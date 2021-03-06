import speech_recognition as sr
from reader import Reader


class AudioReader(Reader):
    """A class based on the speech recognition package for an audio file."""

    RECORD = {
        "en-US": "Is Loading!",
        "fa-IR": "در حال بارگزاری!"
    }

    def __init__(self, audio_file, language='fa-IR', verbose=False):
        super(AudioReader, self).__init__(language, verbose)
        self.audio_file = audio_file

    def read(self):
        audio = self.record(self.audio_file, self.language)
        return self.recognize_google(audio, self.language)

    def record(self, audio_file, language):
        with sr.AudioFile(audio_file) as source:
            self._print(self.RECORD.get(language, ''), self.verbose)
            return self.r.record(source)
