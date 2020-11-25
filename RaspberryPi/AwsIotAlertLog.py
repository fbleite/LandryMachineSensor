from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from datetime import datetime
from datetime import timedelta
import numpy as np
import logging
from SimpleAlertLog import SimpleAlertLog


class AwsIotAlertLog(SimpleAlertLog):

    def __init__(self, args):
        self.myMQTTClient = AWSIoTMQTTClient(args.clientId)
        self.myMQTTClient.configureEndpoint("at7s71dzarby8-ats.iot.us-east-1.amazonaws.com", 8883)
        self.myMQTTClient.configureCredentials(args.rootCAPath,
                                               args.privateKeyPath,
                                              args.certificatePath)
        self.myMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
        self.myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        self.myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
        self.myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
        self.myMQTTClient.connect()
        self.lastAlertedSoundIntensity = 0
        self.lastTimeAlerted = datetime.now()


    def alertCurrentStatus(self, laundryMachineStatus):
        super().alertCurrentStatus(laundryMachineStatus)
        if shouldAlertAws(self.lastAlertedStatus, self.lastTimeAlerted, laundryMachineStatus, datetime.now()):
            logging.info("publishing to AWS")
            self.myMQTTClient.publish("sensor/laundry_machine_status", laundryMachineStatus.generateJsonStatus(), 0)
            self.lastAlertedSoundIntensity = laundryMachineStatus.currentSoundIntensity


def shouldAlertAws(lastAlertedSoundIntensity, lastTimeAlerted, currentLMS, currentTime):
    if lastAlertedSoundIntensity == None:
        return True
    if currentLMS.statusChanged:
        return True
    if currentLMS.isRunning:
        return True
    if currentTime - lastTimeAlerted > timedelta(minutes=60):
        return True
    if np.abs(currentLMS.currentSoundIntensity - lastAlertedSoundIntensity) > 1:
        return True
    return False

