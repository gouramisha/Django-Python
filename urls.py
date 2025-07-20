# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('room1/', views.chat_room, name='chat_room'),
]
