import string
from typing import Callable, TypeVar

from audio.text_reader import TextReader


class Command:
    T = TypeVar('T')

    def __init__(self, phrase: str, func: Callable[[], T], text_confirmation: str = ''):
        words = map(lambda x: x.strip(string.punctuation), phrase.lower().split())
        self.phrase = ' '.join(words)
        self.func = func
        self.text_confirmation = text_confirmation
        self.text_reader = TextReader()

    def is_some_phrase(self, phrase: str) -> bool:
        words = map(lambda x: x.strip(string.punctuation), phrase.lower().split())
        clean_phrase = ' '.join(words)
        return self.phrase == clean_phrase

    def execute(self) -> T:
        if self.text_confirmation:
            self.text_reader.say(self.text_confirmation)
        return self.func()
