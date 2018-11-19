from SimpleAlertLog import SimpleAlertLog
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging

class AwsIotAlertLog(SimpleAlertLog):

    def __init__(self):
        self.myMQTTClient = AWSIoTMQTTClient("MacbookPro")
        self.myMQTTClient.configureEndpoint("at7s71dzarby8-ats.iot.us-east-1.amazonaws.com", 8883)
        self.myMQTTClient.configureCredentials("/Users/fbleite/Development/iotPlayground/root-CA.crt",
                                          "/Users/fbleite/Development/iotPlayground/MacbookPro.private.key",
                                          "/Users/fbleite/Development/iotPlayground/MacbookPro.cert.pem")
        self.myMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
        self.myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        self.myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
        self.myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
        self.myMQTTClient.connect()

    def alertCurrentStatus(self, laundryMachineStatus):
        super().alertCurrentStatus(laundryMachineStatus)
        logging.info('Super duper')
        self.myMQTTClient.publish("sensor/laundry_machine_status", laundryMachineStatus.generateJsonStatus(), 0)