from django.urls import path, include
from rest_framework import routers
from .views import ConversationViewSet, MessageViewSet, protected_view


router = routers.DefaultRouter()

router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('protected/', protected_view),
]