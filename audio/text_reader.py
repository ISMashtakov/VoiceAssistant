import pyttsx3


class TextReader:
    def __init__(self):
        self.engine = pyttsx3.init()

    def say(self, text: str):
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()
