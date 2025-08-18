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
