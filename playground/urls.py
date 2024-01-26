from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.welcome),
    path('hello/<str:name>/', views.hello_user),
    path('play/<str:number>/', views.playground_1)
]