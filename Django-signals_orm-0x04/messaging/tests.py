from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class MessagingNotificationTestCase(TestCase):

    def setUp(self):
        # Créer deux utilisateurs
        self.sender = User.objects.create_user(username='alice', password='testpass123')
        self.receiver = User.objects.create_user(username='bob', password='testpass123')

    def test_message_creation_creates_notification(self):
        # Vérifie qu'il n'y a pas de notifications au départ
        self.assertEqual(Notification.objects.count(), 0)

        # Créer un message
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content='Bonjour Bob, voici un message.'
        )

        # Vérifie que le message a bien été créé
        self.assertEqual(Message.objects.count(), 1)

        # Vérifie qu'une notification a bien été créée
        self.assertEqual(Notification.objects.count(), 1)

        # Vérifie que la notification est bien liée au bon utilisateur et message
        notification = Notification.objects.first()
        self.assertEqual(notification.user, self.receiver)
        self.assertEqual(notification.message, message)
        self.assertFalse(notification.is_read)

    def test_multiple_messages_create_multiple_notifications(self):
        Message.objects.create(sender=self.sender, receiver=self.receiver, content="Message 1")
        Message.objects.create(sender=self.sender, receiver=self.receiver, content="Message 2")

        self.assertEqual(Message.objects.count(), 2)
        self.assertEqual(Notification.objects.count(), 2)

    def test_no_notification_created_on_message_update(self):
        message = Message.objects.create(sender=self.sender, receiver=self.receiver, content="Original")
        notification_count = Notification.objects.count()

        # Modifier le message
        message.content = "Modifié"
        message.save()

        # Le nombre de notifications ne doit pas changer
        self.assertEqual(Notification.objects.count(), notification_count)
