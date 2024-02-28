from django.shortcuts import render, redirect
from django.urls import reverse


def room(request):
    return render(request, 'chat/room.html')

