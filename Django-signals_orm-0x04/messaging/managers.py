from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

@login_required
def unread_inbox(request):
    user = request.user

    # Récupère les messages non lus uniquement, avec optimisation .only()
    unread_messages = Message.unread.for_user(user).select_related('sender')

    return render(request, 'inbox_unread.html', {'messages': unread_messages})