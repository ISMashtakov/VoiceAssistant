from typing import List, Optional, Dict, Iterator, Tuple

from .command import Command
from .semantic_proximity import Embedding, SemanticController


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
    EXACTLY_THRESHOLD = 0.2
    NOT_SURE_THRESHOLD = 0.35

    def __init__(self, commands: Optional[List[Command]] = None):
        self.__semantic_controller = SemanticController()
        self.commands = _Commands()

        if commands:
            for command in commands:
                for phrase in command.phrases:
                    embedding = self.__semantic_controller.get_embedding(phrase)
                    self.commands[embedding] = command

    def execute(self, text: str):
        closest, dist = self.__semantic_controller.get_closest(
            self.__semantic_controller.get_embedding(text),
            self.commands.keys()
        )
        if dist <= self.EXACTLY_THRESHOLD:
            self.commands[closest].execute()
            return
        if dist <= self.NOT_SURE_THRESHOLD:
            print(f'Вы имели ввиду: {closest}?')
            return

