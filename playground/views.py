
from django.shortcuts import render
from django.http import HttpResponse, BadHeaderError
from django.core.mail import send_mail, send_mass_mail, EmailMessage


# Create your views here.
def welcome(request):
    return HttpResponse("welsome to django")


def hello_user(request, name):
    try:
        message = f'Hello {name}warning', 'stop send rubbish mail'
        send_mail("warning", message, 'complaints@tweeter.com',['yila@tweeter.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {"name": name})


def playground_1(request, number):
    return render(request, 'play.html', {"number": number})
