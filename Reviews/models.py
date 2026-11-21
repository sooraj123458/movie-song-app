from django.db import models

# Create your models here.

from Accounts.models import User

from Movie.models import Movie

from Songs.models import Song

class Review(models.Model):

    RATING_CHOICES = (
        ('⭐','⭐'),
        ('⭐⭐','⭐⭐'),
        ('⭐⭐⭐','⭐⭐⭐'),
        ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐')
    )

    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='review')

    rating = models.CharField(max_length=400,choices=RATING_CHOICES)

    comment = models.TextField()

    created_at =models.DateTimeField(auto_now_add=True,null=True)

    updated_at =  models.DateTimeField(auto_now=True,null=True)



