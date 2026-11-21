from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    ROLES = (
        ('admin','admin'),
        ('user','user')
    )

    role = models.CharField(max_length=20,choices=ROLES,default='user')

    phone = models.CharField(max_length=12,unique=True)