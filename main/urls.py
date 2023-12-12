from django.urls import path
from . import views

urlpatterns = [
    path('green/', views.green, name='green'),
    path('blue/', views.blue, name='blue'),
    path('red/', views.red, name='red'),
    path('file_upload/', views.file_upload, name='file_upload'),
    path('send_mqtt_message_train_run/', views.send_mqtt_message_train_run, name='send_mqtt_message_train_run'),
    path('send_mqtt_message_train_run_auto/', views.send_mqtt_message_train_run_auto, name='send_mqtt_message_train_run_auto'),
    path('send_mqtt_message_train_stop/', views.send_mqtt_message_train_stop, name='send_mqtt_message_train_stop'),
    path('/send_mqtt_message/', views.send_mqtt_message, name='send_mqtt_message'),
    path('/send_mqtt_message_no_cal/', views.send_mqtt_message_no_cal, name='send_mqtt_message_no_cal'),
    path('/message/<str:topic>/', views.latest_message, name='latest_message'),
    path('/device', views.home, name='main-home'),
    path('/about/', views.about, name='main-about'),
]
