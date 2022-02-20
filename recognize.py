import speech_recognition as sr

from audio.text_reader import TextReader
from helpers.text_helper import clean_phrase


class Recognizer:
    def __init__(self, name: str, language: str = 'ru-RU'):
        self.name = name
        self.language = language
        self._recognition = sr.Recognizer()
        self._text_reader = TextReader()

    def print_detected_phrase(self):
        self._text_reader.say("Привет")
        print("Я тебя услышал!")

    @staticmethod
    def print_detecting_phrase():
        print("Слушаю")

    def is_welcome_phrase(self, phrase: str) -> bool:
        return f"привет {self.name}".lower() in clean_phrase(phrase)

    def wait_name(self):
        with sr.Microphone() as mic:
            while True:
                self.print_detecting_phrase()
                self._recognition.adjust_for_ambient_noise(mic)
                audio = self._recognition.listen(mic)
                try:
                    text = self._recognition.recognize_google(audio, language=self.language)
                except Exception as ex:
                    print(ex)
                    continue
                if self.is_welcome_phrase(text):
                    self.print_detected_phrase()
                    break

    def get_next_command(self) -> str:
        self.wait_name()
        with sr.Microphone() as mic:
            self.print_detecting_phrase()
            self._recognition.adjust_for_ambient_noise(mic)
            audio = self._recognition.listen(mic)
            try:
                return self._recognition.recognize_google(audio, language=self.language)
            except Exception as ex:
                print(ex)
                return ''
