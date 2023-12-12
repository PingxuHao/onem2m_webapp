import paho.mqtt.client as mqtt
from main.models import MQTTMessage

def on_connect(client, userdata, flags, rc):
    client.subscribe("#")




def on_message(client, userdata, msg):
    MQTTMessage.objects.create(
        topic=msg.topic,
        payload=msg.payload.decode("utf-8"),  # assuming payload is a string
        is_base64_encoded=False  # Update this based on your use case
    )

    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


def start_mqtt_client():
    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_start() 
start_mqtt_client()