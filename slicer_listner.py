import os
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILENAME = "received_file"

# Function to handle the incoming MQTT messages
def on_message(client, userdata, msg):
    # Check if we received the EOF message
    if msg.payload == b'EOF':
        print("File received successfully.")
        client.disconnect()
    else:
        with open(OUTPUT_FILENAME, 'ab') as f:
            f.write(msg.payload)
            print("Received a chunk and wrote to file.")

# Connect to the MQTT server
client = mqtt.Client()
client.on_message = on_message

client.connect(MQTT_SERVER, MQTT_PORT, 60)
client.subscribe(SUBSCRIBE_TOPIC, qos=1)

# Start the MQTT client
client.loop_forever()
