from django.shortcuts import render
from .models import Device
from django.views.generic import ListView, DetailView


class DeviceListView(ListView):
    model = Device
    template_name = 'devices/device_list.html'
    context_object_name = 'devices'

class DeviceDetailView(DetailView):
    model = Device

