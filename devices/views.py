from django.shortcuts import render
from .models import Device
from django.views.generic import ListView, DetailView,TemplateView
from django.http import JsonResponse
from django.shortcuts import render
from .models import MQTTMessage
# devices/mqtt.py or main/mqtt.py
from django.http import JsonResponse

# mqtt_client.py
import paho.mqtt.client as mqtt
def button_click_ON(request):
    print("led turned on")
    # This view is called when the button is clicked
    if request.method == 'POST':
        cmd = "ON"
        send(cmd)
        print("yes")
        return JsonResponse({'status': 'Message sent'})
    else:
        # Handle unexpected HTTP method
        print("error at send ")
        return JsonResponse({'status': 'Error'}, status=405)
    
def button_click_OFF(request):
    print("led turned off")
    # This view is called when the button is clicked
    if request.method == 'POST':
        cmd = "no"
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
        message = 'yes'
    else:
        message = 'no'
        
    MQTT_SERVER = "52.14.47.13"
    MQTT_PORT = 1883
    PUBLISH_TOPIC = "/ESP32/Update"
    message_json = json.dumps(message, separators= (",", ":"))
    client = mqtt.Client()
    client.connect(MQTT_SERVER, MQTT_PORT, 60)
    client.publish(PUBLISH_TOPIC, message_json)
    client.loop_start()
    client.disconnect()


def publish_message(message):
    send(message)  # Call the send function from sender.py


# def display_messages(request):
#     messages = MQTTMessage.objects.all()
#     return render(request, 'messages.html', {'messages': messages})

class DeviceListView(ListView):
    model = Device
    template_name = 'devices/device_list.html'
    context_object_name = 'devices'

class DeviceDetailView(DetailView):
    model = Device
class MyProjectView(TemplateView):
    template_name = 'my_project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any context variables you want to pass to the template here
        return context

