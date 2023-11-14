# mqtt_client.py
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
MQTT_TOPIC = "ESP32/Update"

client = mqtt.Client()
client.connect(MQTT_SERVER, MQTT_PORT, 60)

def publish_message(message):
    print("message published")
    client.publish(MQTT_TOPIC, message)
