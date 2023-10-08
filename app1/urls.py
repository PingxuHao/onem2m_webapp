from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello_world),
    path("about", views.about, name = 'about'),
    path('device_detail/<str:device_name>/', views.device_detail, name='device_detail')
]