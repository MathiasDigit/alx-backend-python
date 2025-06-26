from django.db import models
from django.contrib.auth.models import AbstractUser 
import uuid




# Create your models here.
class User(AbstractUser, models.Model):
    user_id = models.BigAutoField(primary_key=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    
class Conversation(models.Model):
    conversation_id = models.BigAutoField(primary_key=True)
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    
class Message(models.Model):
    message_id = models.BigAutoField(primary_key=True)
    sender_id =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=True)

