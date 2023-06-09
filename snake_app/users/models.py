from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.EmailField(unique=True, null=False)
    phone_number = models.CharField(max_length=24, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []