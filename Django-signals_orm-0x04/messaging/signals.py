from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Message, MessageHistory, MessageHistory

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Message.objects.get(pk=instance.pk)
            if old_instance.content != instance.content:
                # Enregistrer l'ancien contenu
                MessageHistory.objects.create(
                    message=instance,
                    old_content=old_instance.content
                )
                instance.edited = True
        except Message.DoesNotExist:
            pass  # Nouveau message, ne rien faire

@receiver(post_delete, sender=User)
def clean_user_data(sender, instance, **kwargs):
    # Les messages et notifications devraient déjà être supprimés via CASCADE.
    # On nettoie les historiques orphelins si jamais il en reste (par sécurité).
    Message.objects.filter(message__sender=instance).delete()
    Message.objects.filter(message__receiver=instance).delete()
