from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


# Create your tests here.

class TestTweetEndPoint:
    def test_that_anonymous_returns_401(self):
        client = APIClient
        response = client.post('/tweets/', {'text': 'b'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_that_anonymous_returns_201(self):
    client = APIClient
    client.force_authenticate(user={})
    response = client.post('/tweets/', {'text': 'b'})
    assert response.status_code == status.HTTP_201_CREATED
