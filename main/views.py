from django.shortcuts import render
from .models import MQTTMessage

# devices/mqtt.py or main/mqtt.py
from django.http import JsonResponse

def button_click_ON(request):
    print("led turned on")
    # This view is called when the button is clicked
    if request.method == 'POST':
        cmd = "ON"
        send(cmd)
        print("led turned on")
        return JsonResponse({'status': 'Message sent'})
    else:
        # Handle unexpected HTTP method
        print("error at send ")
        return JsonResponse({'status': 'Error'}, status=405)
def button_click_OFF(request):
    print("led turned off")
    # This view is called when the button is clicked
    if request.method == 'POST':
        cmd = "OFF"
        send(cmd)
        print("led turned OFF")
        return JsonResponse({'status': 'Message sent'})
    else:
        # Handle unexpected HTTP method
        print("error at send ")
        return JsonResponse({'status': 'Error'}, status=405)
    
    
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

def home(request):
    context = {
        
    }
    return render(request, 'main/home.html', context)


def about(request):
    return render(request, 'main/about.html', {'title': 'About'})
