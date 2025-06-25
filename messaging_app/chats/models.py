from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.conf import settings



# Create your models here.
class User(AbstractUser):
    user_id = models.BigAutoField(primary_key=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    
class Conversation(models.Model):
    conversation_id = models.BigAutoField(primary_key=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    
class Message(models.Model):
    message_id = models.BigAutoField(primary_key=True)
    sender_id =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=True)

