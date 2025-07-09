from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsParticipantOfConversation
from .filters import MessageFilter
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied

# Create your views here.
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_class = [IsAuthenticated, IsParticipantOfConversation] # Ensure only owners can access messages
    pagination_class = CustomPagination # Enable pagination for messages
    filter_backends = [DjangoFilterBackend]  # Enable django-filter backend
    filterset_class = MessageFilter  # Apply custom filter clas
    
    def get_queryset(self):
        queryset = Message.objects.filter(conversation__participants=self.request.user)

         # Filtrer par conversation_id si présent dans les paramètres de requête
        conversation_id = self.request.query_params.get('conversation_id')
        if conversation_id:
            try:
                conversation = Conversation.objects.get(id=conversation_id)
                if self.request.user not in conversation.pariticoants.all():
                    raise PermissionDenied("You are not a participant of this conversation.")
                queryset = queryset.filter(conversation=conversation)
            except Conversation.DoesNotExist:
                return Message.objects.none()

        return queryset 


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]




    
