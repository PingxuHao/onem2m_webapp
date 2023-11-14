import os
import paho.mqtt.client as mqtt
import time
# MQTT setup
MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
PUBLISH_TOPIC = "/update/esp32"

# File info
#FILE_PATH = "iphoneSpam.ino.ino.bin"
FILE_PATH = "tester.jpg"
CHUNK_SIZE = 1024*48

# Initialize MQTT client
client = mqtt.Client()
client.connect(MQTT_SERVER, MQTT_PORT, 60)

def file_to_chunks(file_path, chunk_size):
    
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# Publish file in chunks
def publish_file(file_path, chunk_size):
    for i, chunk in enumerate(file_to_chunks(file_path, chunk_size)):
        time.sleep (1)
        chunk_topic = f"{PUBLISH_TOPIC}/{i:04d}"
        client.publish(PUBLISH_TOPIC, chunk)
        print(f"Published chunk {i}")
    # Send a message to indicate the end of the file
    
    client.publish(PUBLISH_TOPIC, "EOF")

publish_file(FILE_PATH, CHUNK_SIZE)

# Disconnecting the client
client.disconnect()
