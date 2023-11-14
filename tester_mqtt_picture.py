import os
import paho.mqtt.client as mqtt
MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
SUBSCRIBE_TOPIC = "esp32_update"
OUTPUT_FILENAME = "received.bin"

def on_message(client, userdata, msg):
    with open(OUTPUT_FILENAME, 'ab') as f:
        f.write(msg.payload)
        print("Received a chunk and wrote to file.")
        client.disconnect()
client = mqtt.Client()
client.on_message = on_message

client.connect(MQTT_SERVER, MQTT_PORT, 60)
client.subscribe(SUBSCRIBE_TOPIC, qos=1)
client.loop_forever()
