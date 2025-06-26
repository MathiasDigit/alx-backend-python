from django.urls import path, include
from rest_framework import routers
from .views import ConvesationViewSet, MesssageViewSet

router = routers.DefaultRouter()

router.register(r'conversations', ConvesationViewSet)
router.register(r'messages', MesssageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]