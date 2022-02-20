from typing import List, Optional, Dict, Iterator, Tuple

from audio.text_reader import TextReader
from .command import Command
from .semantic_proximity import Embedding, SemanticController
from recognize import Recognizer


class _Commands(Dict[Embedding, Command]):
    def __init__(self, commands: Optional[Iterator[Tuple[Embedding, Command]]] = None):
        super().__init__()
        if commands is not None:
            for embedding, command in commands:
                self.__setitem__(embedding, command)

    def __setitem__(self, key: Embedding, value: Command):
        if not isinstance(key, Embedding):
            raise ValueError('key should be Embedding')
        if not isinstance(value, Command):
            raise ValueError('value should be Command')
        super().__setitem__(key, value)


class CommandExecutor:
    EXACTLY_THRESHOLD = 0.3
    NOT_SURE_THRESHOLD = 0.5

    def __init__(self, recognizer: Recognizer,  commands: Optional[List[Command]] = None):
        self.__recognizer = recognizer
        self.__semantic_controller = SemanticController()
        self.__text_reader = TextReader()
        self.commands = _Commands()

        if commands:
            for command in commands:
                for phrase in command.phrases:
                    embedding = self.__semantic_controller.get_embedding(phrase)
                    self.commands[embedding] = command

        self.yes_embedding = self.__semantic_controller.get_embedding('да')
        self.no_embedding = self.__semantic_controller.get_embedding('нет')

    def _confirm_not_sure_command(self, command: Embedding) -> bool:
        self.__text_reader.say(f'Вы имели ввиду: {command}?')
        text = self.__recognizer.get_next_text()
        answer, dist = self.__semantic_controller.get_closest(
            self.__semantic_controller.get_embedding(text),
            [self.yes_embedding, self.no_embedding]
        )
        return answer is self.yes_embedding and dist < self.EXACTLY_THRESHOLD

    def execute(self, text: str):
        closest, dist = self.__semantic_controller.get_closest(
            self.__semantic_controller.get_embedding(text),
            self.commands.keys()
        )
        if dist <= self.EXACTLY_THRESHOLD:
            self.commands[closest].execute()
            return
        if dist <= self.NOT_SURE_THRESHOLD:
            if self._confirm_not_sure_command(closest):
                self.commands[closest].execute()
            return

