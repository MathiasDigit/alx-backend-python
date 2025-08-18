from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

@login_required
def delete_user(request):
    user = request.user
    logout(request)  # Déconnecte l'utilisateur
    user.delete()    # Supprime le compte utilisateur
    return redirect('home')  # Redirige vers la page d'accueil après suppression

@login_required
def inbox_view(request):
    user = request.user

    # Récupérer les messages "originaux" reçus (pas des réponses)
    messages = Message.objects.filter(receiver=user, parent_message__isnull=True) \
        .select_related('sender') \
        .prefetch_related('replies__sender') \
        .order_by('-timestamp')

    return render(request, 'inbox.html', {'messages': messages})

@login_required
def unread_inbox(request):
    user = request.user

    # Récupère les messages non lus uniquement, avec optimisation .only()
    unread_messages = Message.unread.for_user(user).select_related('sender')

    return render(request, 'inbox_unread.html', {'messages': unread_messages})
["Message.unread.unread_for_user"]