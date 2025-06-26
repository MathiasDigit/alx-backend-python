from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ConvesationViewSet, MesssageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'conversations', ConvesationViewSet)
router.register(r'messages', MesssageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]