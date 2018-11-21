# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("MacbookPro")
# For Websocket connection
# myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
# Configurations
# For TLS mutual authentication
myMQTTClient.configureEndpoint("at7s71dzarby8-ats.iot.us-east-1.amazonaws.com", 8883)
# For Websocket
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
# For TLS mutual authentication with TLS ALPN extension
# myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
myMQTTClient.configureCredentials("/Users/fbleite/Development/iotPlayground/root-CA.crt",
                                  "/Users/fbleite/Development/iotPlayground/MacbookPro.private.key",
                                  "/Users/fbleite/Development/iotPlayground/MacbookPro.cert.pem")
# For Websocket, we only need to configure the root CA
# myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
myMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

print ('starting')
myMQTTClient.connect()
print ('subscribing')
myMQTTClient.subscribe("sensor/keepalive", 1, customCallback)
time.sleep(1)

for i in range (10) :
    print('publish ' , i)
    myMQTTClient.publish("sensor/laundry_machine_status", "myPayload" + str(i), 0)
    time.sleep(1)

myMQTTClient.unsubscribe("sensor/keepalive")
myMQTTClient.disconnect()