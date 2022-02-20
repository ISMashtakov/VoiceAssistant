from recognize import Recognizer
from command_executor.command_executor import CommandExecutor
from command_executor.commands import ALL_COMMANDS

NAME = "Пятница"


if __name__ == '__main__':
    recognizer = Recognizer(NAME)
    executor = CommandExecutor(recognizer, ALL_COMMANDS)
    while True:
        command_text = recognizer.get_next_command()
        print(command_text)
        executor.execute(command_text)

