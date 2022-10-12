from django.urls import path
from .views import MusicAppCreate

urlpatterns = [
    path('', MusicAppCreate.as_view()),
]