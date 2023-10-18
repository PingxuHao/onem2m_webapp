from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('send_mqtt_on/', views.button_click_ON, name='send_mqtt_on'),
    path('send_mqtt_off/', views.button_click_OFF, name='send_mqtt_off'),
    path('about/', views.about, name='main-about'),
]
