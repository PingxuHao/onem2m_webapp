import paho.mqtt.client as mqtt

# MQTT server details
MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
MQTT_TOPIC = "ESP32/Update"  # You should change this to your specific topic
MQTT_MSG = "yes"


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.publish(MQTT_TOPIC, "yes")
    

def on_publish(client, userdata, mid):
    print("Message Published...")
    client.disconnect()

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

client = mqtt.Client()


client.on_connect = on_connect
client.on_publish = on_publish
client.on_disconnect = on_disconnect

# Connect to the MQTT broker
client.connect(MQTT_SERVER, MQTT_PORT, 60)
client.loop_forever()
