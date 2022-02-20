from recognize import Recognizer
from command_executor.command import Command
from command_executor.command_executor import CommandExecutor

from windows_sound_manager.keyboard import Keyboard

NAME = "Пятница"

if __name__ == '__main__':
    recognizer = Recognizer(NAME)
    executor = CommandExecutor([

    ])
    while True:
        command_text = recognizer.get_next_command()
        print(command_text)
        executor.execute(command_text)

