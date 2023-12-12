from django.apps import AppConfig

class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        from .mqtt_client import start_mqtt_client
        start_mqtt_client()
