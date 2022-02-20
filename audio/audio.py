import simpleaudio as sa

from .text_reader import TextReader


class Audio:
    def __init__(self):
        self.__reader = TextReader()
        self.signal = sa.WaveObject.from_wave_file("resources/signal.wav")

    def say(self, text: str):
        self.__reader.say(text)

    def play_signal(self):
        play_obj = self.signal.play()
        play_obj.wait_done()
