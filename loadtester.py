import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
import paho.mqtt.client as mqtt

MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
#SUBSCRIBE_TOPIC = "/oneM2M/resp/aqm/capstone-iot/json"
SUBSCRIBE_TOPIC = "/update/esp32"
OUTPUT_FILE = "messages.txt"  
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)

def on_message(client, userdata, msg):
    message = f"Received message: {msg.payload.decode()} on topic {msg.topic} with QoS {msg.qos}"

    with open(OUTPUT_FILE, 'a') as file: 
        file.write(message + '\n\n')  
    print("Message written to file.")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, 60)

# Start the loop
client.loop_forever()
