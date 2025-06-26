"""Serializers for chat application models."""
from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    has_phone = serializers.SerializerMethodField()

    def get_has_phone(self, obj):
        return bool(obj.phone_number)
    
    def validate_first_name(self, value):
        if ';' in value:
            raise serializers.ValidationError("First name cannot contain semicolons.")
        return value
    def validate_last_name(self, value):
        if ';' in value:
            raise serializers.ValidationError("Last name cannot contain semicolons.")
        return value
    
    class Meta:
        model = User
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField()

    def get_sender(self, obj):
        return obj.sender_id.username
    
    class Meta:
        model = Message
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = '__all__'
    


