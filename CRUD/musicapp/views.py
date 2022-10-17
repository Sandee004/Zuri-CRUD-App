#from django.shortcuts import render
from rest_framework import viewsets
from .models import Songs
from .serializer import SongsSerializer

class SongsViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer