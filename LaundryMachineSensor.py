from AudioProcessing import AudioProcessing
from SimpleAlertLog import SimpleAlertLog as Alert
import numpy as np

ap = AudioProcessing(chunk=1024, rate=44100)
previousIntensities = [0, 0, 0]
wasLaundryMachineRunningBefore = False
threshold = 1500
needsToAlert = False


while True:
    del previousIntensities[0]
    previousIntensities.append(ap.getSoundIntensityForTimebox())
    averageIntensities = np.mean(previousIntensities)
    print('average: ', averageIntensities)
    if averageIntensities < threshold:
        if wasLaundryMachineRunningBefore:
            wasLaundryMachineRunningBefore = False
            needsToAlert = True
    else :
        if wasLaundryMachineRunningBefore == False:
            wasLaundryMachineRunningBefore = True
            needsToAlert = True

    if needsToAlert:
        Alert.alertMachineStatusChanged(Alert, wasLaundryMachineRunningBefore)
        needsToAlert=False



