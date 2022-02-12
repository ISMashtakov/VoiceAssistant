from typing import List


class Microphone:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Recognizer:
    TEXTS = []
    COUNT_LISTEN = 0

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def set_texts(texts: List[str]):
        texts.reverse()
        Recognizer.TEXTS = texts

    def adjust_for_ambient_noise(self,  *args, **kwargs):
        pass

    def listen(self, *args, **kwargs):
        Recognizer.COUNT_LISTEN += 1
        pass

    def recognize_google(self, *args, **kwargs) -> str:
        return Recognizer.TEXTS.pop()