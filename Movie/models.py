from django.db import models

# Create your models here.

from Accounts.models import User
   
class Movie(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    release_date = models.DateField()

    language = models.CharField(max_length=50)

    genre = models.CharField(max_length=100)

    director = models.CharField(max_length=100)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title






