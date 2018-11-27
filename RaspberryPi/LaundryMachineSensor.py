from AudioProcessing import AudioProcessing
# from SimpleAlertLog import SimpleAlertLog as Alert
from AwsIotAlertLog import AwsIotAlertLog as Alert
from LaundryMachineStatus import LaundryMachineStatus
import logging
import argparse

def parseCommandLineArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rootCA", action="store", required=True, dest="rootCAPath", help="Root CA file path")
    parser.add_argument("-c", "--cert", action="store", required=True, dest="certificatePath", help="Certificate file path")
    parser.add_argument("-k", "--key", action="store", required=True, dest="privateKeyPath", help="Private key file path")
    parser.add_argument("-id", "--clientId", action="store", required=True, dest="clientId", help="Targeted client id")
    parser.add_argument("-t", "--threshold", action="store",  dest="threshold", help="Targeted machine On threshold", default=1500)
    args = parser.parse_args()
    return args


def setupLogging():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

setupLogging()
args = parseCommandLineArguments()


logging.info('Starting up!')
ap = AudioProcessing(chunk=8192, rate=44100)
ls = LaundryMachineStatus(threshold=args.threshold)
alert = Alert(args)

while True:
    ls.insertNewSoundIntensity(ap.getSoundIntensityForTimebox())
    alert.alertCurrentStatus(ls)