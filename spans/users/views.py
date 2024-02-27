from django.urls import reverse
from users.models import User
from django.shortcuts import render, redirect
from django.views import View

from users.forms import SignUpForm


class SignupView(View):
    def get(self, request):
        form = SignUpForm()
        content = {
            "form": form,
        }
        return render(request, 'users/signup.html', content)

    def post(self, request):
        form = SignUpForm(request.POST or None)
        if form.is_valid():

            username = form.data['username']
            password = form.data['password1']

            user = User.objects.create_user(username=username, password=password,)
            user.is_active = True
            user.save()
            print("redirect")
            return redirect(reverse('auth:login'))

        content = {
            "form": form,
        }
        return render(request, 'users/signup.html', content)
