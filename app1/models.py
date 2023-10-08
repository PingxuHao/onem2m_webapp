from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# user, device detail, files

class Device(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    
