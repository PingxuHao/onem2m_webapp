import paho.mqtt.client as mqtt
import time
import datetime

# MQTT settings
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC_SUBSCRIBE = "train/status"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC_SUBSCRIBE)
    client.subscribe("train/stop_sig")

# Callback for handling messages from the subscribe topic
def on_subscribe_message(client, userdata, msg):
    if msg.topic == MQTT_TOPIC_SUBSCRIBE:
        print(1)
        client.publish("train/stop_sig", "STOP")
    elif msg.topic == "train/stop_sig" :
        time.sleep(3)
        client.publish("train/stop_sig", "RUN")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_subscribe_message
print(122)
client.connect(MQTT_BROKER, MQTT_PORT, 60)

client.loop_forever()
