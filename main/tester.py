import paho.mqtt.client as mqtt
import json

# MQTT server details
MQTT_SERVER = "52.14.47.13"
MQTT_PORT = 1883
PUBLISH_TOPIC = "/oneM2M/req/aqm/capstone-iot/json"  # replace with your actual publish topic

def send(message):
    client = mqtt.Client()
    client.connect(MQTT_SERVER, MQTT_PORT, 60)
    message_json = json.dumps(message, separators= (",", ":"))
    #message_json =  "{\"to\":\"cse-in\",\"op\":2,\"rqi\":\"Hi from the nRF9160 SiP\",\"rvi\":\"3\",\"fr\":\"CAdmin\"}"
    client.publish(PUBLISH_TOPIC, message_json)
    
    client.loop_start()
    client.disconnect()

# Example usage of the above function
if __name__ == "__main__":
    # Define the message to send
    message = {"to":"cse-in","op":2,"rqi":"LED_ON","rvi":"3","fr":"CAdmin"}

    # Call the function to publish the message
    send(message)

