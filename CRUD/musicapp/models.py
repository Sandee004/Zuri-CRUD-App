from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 100, primary_key = True)
    last_name = models.CharField(max_length = 100)
    age = models.IntegerField()

    #Specifies what will show in the admin dashboard(database)
    def __str__(self):
        return self.first_name

class Songs(models.Model):
    title = models.CharField(max_length = 150, primary_key = True)
    date_released = models.IntegerField()
    likes = models.IntegerField()
    artist_id = models.IntegerField()

    #Specifies what will show in the admin dashboard(database)
    def __str__(self):
        return self.title

class Lyrics(models.Model):
    content = models.TextField(primary_key = True)
    song_id = models.IntegerField()

    #Specifies what will show in the admin dashboard(database)
    def __str__(self):
        return self.song_id