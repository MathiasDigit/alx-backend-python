from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework import permissions
from .models import Conversation

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class IsParticipantOfConversation(BasePermission):
    """The user can only access his own messages/conversations."""
   
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
   
    def has_object_permission(self, request, view, obj):
        Conversation = getattr(obj, 'conversation', None)

        if not Conversation:
           return False
        
        if request.method in ['PUT, PATCH,' 'DELETE', 'GET', 'POST']:
           return request.user in Conversation.participants.all()
    