import string

import speech_recognition as sr


class Recognizer:
    def __init__(self, name: str, language: str = 'ru-RU'):
        self.name = name
        self.language = language
        self._recognition = sr.Recognizer()

    @staticmethod
    def print_detected_phrase():
        print("Я тебя услышал!")

    @staticmethod
    def print_detecting_phrase():
        print("Слушаю")

    def is_welcome_phrase(self, phrase: str) -> bool:
        words = map(lambda x: x.strip(string.punctuation), phrase.lower().split())
        clean_phrase = ' '.join(words)
        return f"привет {self.name}".lower() in clean_phrase

    def wait_name(self):
        with sr.Microphone() as mic:
            while True:
                self.print_detecting_phrase()
                self._recognition.adjust_for_ambient_noise(mic)
                audio = self._recognition.listen(mic)
                text = self._recognition.recognize_google(audio, language=self.language)
                if self.is_welcome_phrase(text):
                    self.print_detected_phrase()
                    break

    def get_next_command(self) -> str:
        self.wait_name()
        with sr.Microphone() as mic:
            self.print_detecting_phrase()
            self._recognition.adjust_for_ambient_noise(mic)
            audio = self._recognition.listen(mic)
            return self._recognition.recognize_google(audio, language=self.language)
