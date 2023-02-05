from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class RoomChat(models.Model):
    name_room = models.CharField(max_length=30, unique=True)
    
    
class History(models.Model):
     message = models.CharField(max_length=30)
     room = models.ForeignKey(RoomChat, on_delete=models.CASCADE)
     user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
     
     