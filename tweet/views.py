from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Tweet, Comment
from .serializers import TweetSerializer, CommentSerializer
from django.shortcuts import get_object_or_404


class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.filter()
    serializer_class = TweetSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.select_related('tweet').filter(tweet_id=self.kwargs['tweet_pk'])

#
