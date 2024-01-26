from django.contrib.auth.models import AbstractUser
from django.db import models


class TweeterUser(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):
    location = models.CharField(max_length=100)
    tweeter_user = models.OneToOneField(TweeterUser, on_delete=models.CASCADE, primary_key=True)
