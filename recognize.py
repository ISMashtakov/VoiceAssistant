import speech_recognition as sr


class Recognizer:
    MY_NAME = "Пятница"
    LANGUAGE = 'ru-RU'

    def __init__(self):
        self._recognition = sr.Recognizer()

    def test(self):
        with sr.Microphone() as mic:
            self._recognition.adjust_for_ambient_noise(mic)
            audio = self._recognition.listen(mic)
        print(self._recognition.recognize_google(audio, language=Recognizer.LANGUAGE))

    def wait_name(self):
        with sr.Microphone() as mic:
            while True:
                self._recognition.adjust_for_ambient_noise(mic)
                audio = self._recognition.listen(mic)
                text = self._recognition.recognize_google(audio, language=Recognizer.LANGUAGE)
                if f"Привет {Recognizer.MY_NAME}".lower() in str(text).lower():
                    print("Я тебя услышал!")
                    break

    def get_next_command(self) -> str:
        self.wait_name()
        with sr.Microphone() as mic:
            self._recognition.adjust_for_ambient_noise(mic)
            audio = self._recognition.listen(mic)
