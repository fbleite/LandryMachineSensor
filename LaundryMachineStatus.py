import numpy as np

class LaundryMachineStatus:
    def __init__(self, threshold) :
        self.threshold = threshold
        self.previousIntensities = [0, 0, 0]
        self.isRunning = False
        self.statusChanged = False
        self.currentSoundIntensity = 0

    def insertNewSoundIntensity(self, soundIntensity):
        del self.previousIntensities[0]
        self.previousIntensities.append(soundIntensity)
        self.currentSoundIntensity = np.mean(self.previousIntensities)
        self.__calculateNewStatus()

    def __calculateNewStatus(self):
        self.statusChanged = False
        if self.currentSoundIntensity < self.threshold:
            if self.isRunning == True:
                self.isRunning = False
                self.statusChanged = True
        else:
            if self.isRunning == False:
                self.isRunning = True
                self.statusChanged = True