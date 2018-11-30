import numpy as np
import json
import datetime

class LaundryMachineStatus:
    def __init__(self, threshold) :
        self.threshold = threshold
        self.previousIntensities = [0] * 50
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

    def generateAlertMessage (self) :
        message = 'Machine is: '
        if self.isRunning:
            message += 'ON'
        else :
            message += 'OFF'
        message += ' | '
        message += ' Status has changed : ' + str(self.statusChanged)
        message += ' | '
        message += 'Current intensity is: ' + str(self.currentSoundIntensity)
        return message

    def generateJsonStatus(self):
        return json.dumps({'machineStatusOn': self.isRunning,
                           'hasStatusChanged': self.statusChanged,
                           'currentIntensity': self.currentSoundIntensity,
                           'timestamp': datetime.datetime.now().isoformat(),
                           'deviceId': 1})
