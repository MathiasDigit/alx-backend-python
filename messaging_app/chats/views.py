from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsParticipantOfConversation
from .filters import MessageFilter
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_class = [IsAuthenticated, IsParticipantOfConversation] # Ensure only owners can access messages
    pagination_class = CustomPagination # Enable pagination for messages
    filter_backends = [DjangoFilterBackend]  # Enable django-filter backend
    filterset_class = MessageFilter  # Apply custom filter clas
    
    def get_queryset(self):
        user = self.request.user 
        return Message.objects.filter(sender=user) | Message.objects.filter(message=user)


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]




    
