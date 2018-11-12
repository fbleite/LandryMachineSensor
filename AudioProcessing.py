import pyaudio
import numpy as np


class AudioProcessing :
    def __init__(self,
                 chunk=1024,
                 # chunk=2048,
                 rate=44100):
        self.chunk = chunk
        self.rate = rate
        self.format = pyaudio.paInt8
        self.channels = 1
        self.timebox = 5 #In seconds
        self.player = pyaudio.PyAudio()

    def getSoundIntensityForTimebox(self):
        allSound = []
        stream = self.player.open(format=self.format, channels=1, rate=self.rate, input=True, frames_per_buffer=self.chunk)
        for i in range(int(self.timebox * self.rate / self.chunk)):
            sound = stream.read(self.chunk, exception_on_overflow= False)
            allSound.extend(np.fromstring(sound, dtype=np.int8))
        stream.stop_stream()
        stream.close()
        print('All Sound')
        print(allSound)
        return self.calculateAbsotuteAverage(allSound)


    def calculateAbsotuteAverage(self, soundArray):
        return np.mean(np.absolute(soundArray))





