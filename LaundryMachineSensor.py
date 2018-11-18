from AudioProcessing import AudioProcessing
from SimpleAlertLog import SimpleAlertLog as Alert
from LaundryMachineStatus import LaundryMachineStatus
import logging


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.info('Starting up!')
ap = AudioProcessing(chunk=8192, rate=44100)
ls = LaundryMachineStatus(threshold=1500)

while True:
    ls.insertNewSoundIntensity(ap.getSoundIntensityForTimebox())
    logging.info('Average: ' + str(ls.currentSoundIntensity))
    if ls.statusChanged == True:
        Alert.alertMachineStatusChanged(Alert, ls.isRunning)
