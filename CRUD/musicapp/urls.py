from django.urls import path
from .views import SongsViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import routers, serializers

router = routers.DefaultRouter()
router.register(r'song', SongsViewSet, basename='song')
urlpatterns = [] + router.urls