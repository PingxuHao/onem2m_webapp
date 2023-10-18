import os
import paho.mqtt.client as mqtt
from ...models import MQTTMessage

# Ensure Django settings are properly set up
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_proj.settings')  # Replace 'your_project_name' with your project's name
import django
django.setup()

# Callback fires when connected to MQTT broker.
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")
    client.subscribe(SUBSCRIBE_TOPIC)  # subscribe on connect/reconnect

# Callback fires when a published message is received.
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print("Received message: ", message)
    userdata['message'] = message  # store message in userdata dict
    client.disconnect()  # Disconnect after receiving the message

def communicate_with_server(message):
    # This dict will store the reply message received in the on_message callback.
    userdata = {'message': None}

    client = mqtt.Client(userdata=userdata)  # userdata can be a dict to store any data you want to access in callbacks
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_SERVER, MQTT_PORT, 60)

    # Publishing
    message_json = json.dumps(message)  # Convert the dictionary to a JSON string
    client.publish(PUBLISH_TOPIC, message_json)

    client.loop_start()  # Start a new thread, making a non-blocking call
    while userdata['message'] is None:  # Wait until the 'message' field is set by the on_message callback
        time.sleep(1)  # Waiting for the message to be received
    client.loop_stop()  # Stop the loop, the job is done

    return userdata['message']
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()
