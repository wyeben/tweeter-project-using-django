from uuid import uuid4

from django.db import models

from django.contrib.auth.models import User


class Tweet(models.Model):
    text = models.CharField(max_length=200)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-last_update']


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    commented_time = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)


