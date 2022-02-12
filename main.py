from recognize import Recognizer
from command_executor.command import Command
from command_executor.command_executor import CommandExecutor

NAME = "Подручный"

if __name__ == '__main__':
    recognizer = Recognizer(NAME)
    executor = CommandExecutor([
        Command('Следующая песня', lambda: print(5), 'Следующая песня')
    ])
    while True:
        command_text = recognizer.get_next_command()
        print(command_text)
        executor.execute(command_text)

