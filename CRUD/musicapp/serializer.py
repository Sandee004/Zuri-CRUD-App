#from django.urls import path
from .models import Songs
from rest_framework import serializers

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['title', 'date_released']