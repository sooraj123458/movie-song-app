from django.db import models

from Movie.models import Movie

from Accounts.models import User

# Create your models here.

class Song(models.Model):

    title = models.TextField()

    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name="songs")

    singer = models.CharField(max_length=200)

    language = models.CharField(max_length=100)

    music_director = models.CharField(max_length=200)

    track_number=models.PositiveIntegerField(default=0)

    lyricist = models.CharField(max_length=100)

    genre = models.CharField(max_length=100)

    duration = models.DurationField(null=True,blank=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):

        return self.title

    def save(self,*args,**kwargs):

        songs_last_object=Song.objects.filter(movie=self.movie).last()

        if songs_last_object:

            self.track_number=songs_last_object.track_number+1

        else:

            self.track_number=1   

        return super().save(*args,**kwargs)

                

    
