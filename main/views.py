from django.shortcuts import render
from .models import MQTTMessage
from django.http import JsonResponse
from django.http import HttpResponse
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

broker_address = "52.14.47.13"  # Your broker address
port = 1883
topic = "update"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def file_upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        file_content = uploaded_file.read()

        # Create a client instance
        client = mqtt.Client()
        client.on_connect = on_connect

        # Connect to the broker
        client.connect(broker_address, port, 60)

        # Publish the content
        client.publish(topic, file_content)

        # Disconnect from the broker
        client.disconnect()

        return HttpResponse("File uploaded and sent successfully.")
    return render(request, 'upload.html')

def send(topic,message):
    MQTT_SERVER = "52.14.47.13"
    MQTT_PORT = 1883
    client = mqtt.Client()
    client.connect(MQTT_SERVER, MQTT_PORT, 60)
    client.publish(topic, message)
    client.loop_start()
    client.disconnect()

def send_mqtt_message(request):
    broker_address = "52.14.47.13"
    broker_port = 1883
    topic = "rpi"
    message = "START"

    try:
        publish.single(topic, message, hostname=broker_address, port=broker_port)
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
    
def send_mqtt_message_no_cal(request):
    broker_address = "52.14.47.13"
    broker_port = 1883
    topic = "train/calibration"
    message = "NO"
    try:
        publish.single(topic, message, hostname=broker_address, port=broker_port)
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

def send_mqtt_message_train_run(request):
    broker_address = "52.14.47.13"
    broker_port = 1883
    topic = "train/command"
    message = "RUN"
    try:
        publish.single(topic, message, hostname=broker_address, port=broker_port)
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
    
def red(request):
    broker_address = "52.14.47.13"
    broker_port = 1883
    topic = "train/target_color"
    message = "RED"
    try:
        publish.single(topic, message, hostname=broker_address, port=broker_port)
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
    
    
def blue(request):
    broker_address = "52.14.47.13"
    broker_port = 1883
    topic = "train/target_color"
    message = "BLUE"
    try:
        publish.single(topic, message, hostname=broker_address, port=broker_port)
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

def green(request):
    broker_address = "52.14.47.13"
    broker_port = 1883
    topic = "train/target_color"
    message = "GREEN"
    try:
        publish.single(topic, message, hostname=broker_address, port=broker_port)
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
    
def send_mqtt_message_train_run_auto(request):
    broker_address = "52.14.47.13"
    broker_port = 1883
    topic = "train/command"
    message = "RUN_AUTO"
    try:
        publish.single(topic, message, hostname=broker_address, port=broker_port)
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})    
    

def send_mqtt_message_train_stop(request):
    broker_address = "52.14.47.13"
    broker_port = 1883
    topic = "train/command"
    message = "STOP"
    try:
        publish.single(topic, message, hostname=broker_address, port=broker_port)
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

def latest_message(request, topic):
    if topic == "calibration":
        message = MQTTMessage.objects.filter(topic="train/calibration").order_by('-timestamp').first()
    else:
        message = MQTTMessage.objects.filter(topic=topic).order_by('-timestamp').first()
    if message:
        data = {'payload': message.payload}
    else:
        data = {'payload': 'No message available'}
    return JsonResponse(data)


def send(cmd):
    import paho.mqtt.client as mqtt
    import json
    if cmd == "ON":
        message = {
        "to": "cse-in",
        "op": 2,
        "rqi": "LED_ON",
        "rvi": "3",
        "fr": "CAdmin"
    }
    else:
        message = {
        "to": "cse-in",
        "op": 2,
        "rqi": "LED_OFF",
        "rvi": "3",
        "fr": "CAdmin"
    }
    MQTT_SERVER = "52.14.47.13"
    MQTT_PORT = 1883
    PUBLISH_TOPIC = "/oneM2M/req/aqm/capstone-iot/json"
    client = mqtt.Client()
    client.connect(MQTT_SERVER, MQTT_PORT, 60)
    message_json = json.dumps(message, separators= (",", ":"))
    client.publish(PUBLISH_TOPIC, message_json)
    client.loop_start()
    client.disconnect()


def publish_message(message):
    send(message)  # Call the send function from sender.py


def display_messages(request):
    messages = MQTTMessage.objects.all()
    return render(request, 'messages.html', {'messages': messages})

from devices.models import Device 

def home(request):
    devices = Device.objects.all()  # Query all Device objects
    context = {
        'devices': devices  # Pass the devices to the context
    }
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})
