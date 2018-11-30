import pyaudio
import numpy as np
import logging

class AudioProcessing :
    def __init__(self, chunk, rate):
        self.chunk = chunk
        self.rate = rate
        self.format = pyaudio.paInt16
        self.channels = 1
        self.timebox = 15 #In seconds
        self.player = pyaudio.PyAudio()

    def getSoundIntensityForTimebox(self):
        allSound = []
        stream = self.player.open(format=self.format, channels=1, rate=self.rate, input=True, frames_per_buffer=self.chunk)
        for i in range(int(self.timebox * self.rate / self.chunk)):
            sound = stream.read(self.chunk, exception_on_overflow= False)
            allSound.extend(np.fromstring(sound, dtype=np.int16))
        stream.stop_stream()
        stream.close()
        return self.calculateAbsotuteAverage(allSound)


    def calculateAbsotuteAverage(self, soundArray):
        return np.mean(np.absolute(soundArray))





