from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):
    return HttpResponse("welsome to django")


def hello_user(request, name):
    return render(request, 'hello.html', {"name": name})


def playground_1(request, number):
    return render(request, 'play.html', {"number": number})
