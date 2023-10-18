from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Device(models.Model):
    id = models.PositiveIntegerField(blank=True, primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    model_name = models.CharField(max_length=100, default='default_model')  # Model or variant of the device
    ip_address = models.GenericIPAddressField(null = True)
    status = models.BooleanField(default=False)  # Online/Offline status
    mac_address = models.CharField(max_length=17, blank=True, null=True)
    imei_number = models.CharField(max_length=15, blank=True, null=True)
    device_type = models.CharField(max_length=50, blank=True, null=True)
    os_version = models.CharField(max_length=50, blank=True, null=True)
    last_seen = models.DateTimeField(blank=True, null=True)
    firmware_version = models.CharField(max_length=100, blank=True, null=True)  # Firmware version if relevant
    storage_capacity = models.PositiveIntegerField(blank=True, null=True)  # Device storage in MB/GB
    ram_capacity = models.PositiveIntegerField(blank=True, null=True)  # RAM capacity in MB/GB
    cpu_info = models.CharField(max_length=100, blank=True, null=True)  # Processor/CPU information
    is_wireless = models.BooleanField(default=True)  # Does the device support wireless connections?
    wireless_protocols = models.CharField(max_length=100, blank=True, null=True)  # e.g., WiFi, Zigbee, LoRa, Bluetooth
    battery_status = models.PositiveIntegerField(blank=True, null=True)  # Battery percentage (if battery powered)

    def __str__(self):
        return " %s's %s." % (self.owner, self.model_name)

