from django.shortcuts import render, redirect
from django.urls import reverse


def room(request):
    if not request.user.is_authenticated:
        return redirect(reverse("auth:signup"))
    return render(request, 'chat/room.html')

