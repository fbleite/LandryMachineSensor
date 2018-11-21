from AudioProcessing import AudioProcessing
# from SimpleAlertLog import SimpleAlertLog as Alert
from AwsIotAlertLog import AwsIotAlertLog as Alert
from LaundryMachineStatus import LaundryMachineStatus
import logging


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting up!')
ap = AudioProcessing(chunk=8192, rate=44100)
ls = LaundryMachineStatus(threshold=1500)
alert = Alert()

while True:
    ls.insertNewSoundIntensity(ap.getSoundIntensityForTimebox())
    alert.alertCurrentStatus(ls)