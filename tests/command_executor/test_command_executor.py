from unittest import TestCase
from unittest.mock import MagicMock

from command_executor.command_executor import CommandExecutor, Command


class TestCommandExecutor(TestCase):
    def test_execute(self):
        expected_mock = MagicMock()
        pattern = 'Тест шаблон'
        executor = CommandExecutor([
            Command('Просто текст', MagicMock()),
            Command('Тестируем шаблон', expected_mock),
            Command('Проверочный паттерн', MagicMock())
        ])

        executor.execute(pattern)

        expected_mock.assert_called()