from django.views.decorators.cache import cache_page
from django.shortcuts import render, get_object_or_404
from .models import Message
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@cache_page(60)  # ⏱️ 60 secondes de cache
@login_required
def conversation_view(request, conversation_id):
    messages = Message.objects.filter(parent_message_id=conversation_id).select_related('sender').order_by('timestamp')

    return render(request, 'conversation.html', {'messages': messages})
