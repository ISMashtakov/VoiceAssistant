from unittest import TestCase
from unittest.mock import patch, MagicMock

from tests.mocks import speech_recognition as sr_mock

from recognize import Recognizer


class TestRecognizer(TestCase):
    def tearDown(self) -> None:
        sr_mock.Recognizer.COUNT_LISTEN = 0
        sr_mock.Recognizer.set_texts([])

    def test_is_welcome_phrase(self):
        recognizer = Recognizer('Имя')
        self.assertTrue(recognizer.is_welcome_phrase('привет имя'))
        self.assertTrue(recognizer.is_welcome_phrase('прИвеТ иМя'))
        self.assertTrue(recognizer.is_welcome_phrase('кстати, прИвеТ, иМя, чуть не забыл'))
        self.assertFalse(recognizer.is_welcome_phrase('привет'))
        self.assertFalse(recognizer.is_welcome_phrase('имя'))
        self.assertFalse(recognizer.is_welcome_phrase('слышь ты'))

    @patch('recognize.sr.Recognizer', sr_mock.Recognizer)
    @patch('recognize.sr.Microphone', sr_mock.Microphone)
    @patch('recognize.Recognizer.print_detected_phrase')
    @patch('recognize.Recognizer.print_detecting_phrase', lambda x: None)
    def test_wait_name(self, print_mock: MagicMock):
        sr_mock.Recognizer.set_texts(['Плохой текст', 'Привет Имя'])

        recognizer = Recognizer('Имя')
        recognizer.wait_name()

        print_mock.assert_called()
        self.assertEqual(sr_mock.Recognizer.COUNT_LISTEN, 2)

    @patch('recognize.sr.Recognizer', sr_mock.Recognizer)
    @patch('recognize.sr.Microphone', sr_mock.Microphone)
    @patch('recognize.Recognizer.print_detected_phrase')
    @patch('recognize.Recognizer.print_detecting_phrase', lambda x: None)
    def test_get_next_command(self, print_mock: MagicMock):
        sr_mock.Recognizer.set_texts(['Плохой текст', 'Привет Имя', 'Команда', 'Иной текст'])
        recognizer = Recognizer('Имя')
        command = recognizer.get_next_command()

        print_mock.assert_called()
        self.assertEqual(command, 'Команда')


