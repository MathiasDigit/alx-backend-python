from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ConvesationViewSet, MesssageViewSet

["NestedDefaultRouter", "ConversationViewSet", "MessageViewSet"]

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'conversations', ConvesationViewSet)
router.register(r'messages', MesssageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]