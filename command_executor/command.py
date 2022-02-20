from typing import Callable, TypeVar, Union, List

from audio.text_reader import TextReader

from helpers.text_helper import clean_phrase


class Command:
    T = TypeVar('T')

    def __init__(self, phrases: Union[List[str], str], func: Callable[[], T], text_confirmation: str = ''):
        if isinstance(phrases, str):
            self.phrases = [clean_phrase(phrases)]
        else:
            self.phrases = list(map(clean_phrase, phrases))
        self.func = func
        self.text_confirmation = text_confirmation
        self.text_reader = TextReader()

    def execute(self) -> T:
        if self.text_confirmation:
            self.text_reader.say(self.text_confirmation)
        return self.func()
