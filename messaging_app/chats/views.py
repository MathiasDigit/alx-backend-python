from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class UserViewset(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MesssageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ConvesationViewset(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
