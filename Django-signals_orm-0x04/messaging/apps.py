from django.apps import AppConfig

class ChatAppConfig(AppConfig):  # Replace ChatApp with your app's name
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'  # Replace with your app's name

    def ready(self):
        import chat.signals  # Replace 'chat' with your app name
