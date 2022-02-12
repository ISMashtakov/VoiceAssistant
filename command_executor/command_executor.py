from typing import List, Optional

from .command import Command


class CommandExecutor:
    def __init__(self, commands: Optional[List[Command]] = None):
        if commands is None:
            commands = []
        self.commands = commands

    def execute(self, text: str):
        for command in self.commands:
            if command.is_some_phrase(text):
                return command.execute()
