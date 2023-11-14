from django.urls import path
from . import views
from .views import DeviceListView, DeviceDetailView,TemplateView
urlpatterns = [
    path('', DeviceListView.as_view(), name='devices'),
    path('/send_mqtt_on/', views.button_click_ON, name='send_mqtt_on'),
    path('/send_mqtt_off/', views.button_click_OFF, name='send_mqtt_off'),
    path('<int:pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('project/', TemplateView.as_view(), name='my_project'),
]
