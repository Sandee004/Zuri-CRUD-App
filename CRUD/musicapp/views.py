#from django.shortcuts import render
from django.views.generic.edit import CreateView
#from .models import TodoApp
from .models import Artiste, Songs, Lyrics

# Create your views here.
class MusicAppCreate(CreateView):
    model = Songs
    fields = ['title', 'artist_id']
    template_name = 'home.html'