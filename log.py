import paho.mqtt.client as mqtt
import time
import datetime

# MQTT settings
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC_SUBSCRIBE = "train/status"
LOG_FILE = "./log.txt"

# Function to trim the log message to the last 10 lines
def trim_log_message(message):
    lines = message.split('\n')
    if len(lines) > 10:
        return '\n'.join(lines[-10:])
    return message

# Function to read the log file
def read_log_file():
    try:
        with open(LOG_FILE, "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

# Function to write to the log file
def write_log_file(message):
    with open(LOG_FILE, "w") as file:
        file.write(message)
    file.close()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC_SUBSCRIBE)
    client.subscribe("log")

# Callback for handling messages from the subscribe topic
def on_subscribe_message(client, userdata, msg):
    if msg.topic == MQTT_TOPIC_SUBSCRIBE and msg.payload.decode() == "STOP":
        print(1)
        # Read the current log, append new information, and write back
        current_log_message = read_log_file()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        update_message = current_log_message + "\n" + current_time + " Collecting Fruit"
        trimmed_message = trim_log_message(update_message)
        write_log_file(trimmed_message)
        client.publish("log", trimmed_message)
        
    elif msg.topic == "log" and msg.payload.decode()[-1] == 't':
        time.sleep(3)
        current_log_message = read_log_file()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        update_message = current_log_message + "\n" + current_time + " finished collection, train running"
        trimmed_message = trim_log_message(update_message)
        write_log_file(trimmed_message)
        client.publish("log", trimmed_message)

        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_subscribe_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)

client.loop_forever()
