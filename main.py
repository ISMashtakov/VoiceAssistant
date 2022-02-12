from recognize import Recognizer
from command_executor.command import Command
from command_executor.command_executor import CommandExecutor

from windows_sound_manager.keyboard import Keyboard

NAME = "Подручный"

if __name__ == '__main__':
    recognizer = Recognizer(NAME)
    executor = CommandExecutor([
        Command('Включи следующую песню', lambda: Keyboard.keyDown(Keyboard.VK_MEDIA_NEXT_TRACK), 'Следующая песня')
    ])
    while True:
        command_text = recognizer.get_next_command()
        print(command_text)
        executor.execute(command_text)

