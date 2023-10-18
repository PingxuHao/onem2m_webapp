from django.db import models

class MQTTMessage(models.Model):
    topic = models.CharField(max_length=255)
    payload = models.TextField()
    is_base64_encoded = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)