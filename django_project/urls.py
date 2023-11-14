from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from users import views as user_views
from devices import views as device_views


# urlpatterns = [
#     path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
#     path('admin/', admin.site.urls),
#     path('', include('main.urls')),
#     path('device', include('devices.urls')),
#     path('register/', user_views.register, name = 'register'),
#     path('profile/', user_views.profile, name = 'profile'),
# ]
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('admin/', admin.site.urls),
    path('main', include('main.urls')),
    path('device', include('devices.urls')),
    path('register/', user_views.register, name = 'register'),
    path('profile/', user_views.profile, name = 'profile'),
]