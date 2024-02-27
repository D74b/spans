import django.contrib.auth.views
from django.urls import path

import users.views

app_name = "auth"

urlpatterns = [
    path("signup/", users.views.SignupView.as_view(), name="signup"),
    path(
        "login/",
        django.contrib.auth.views.LoginView.as_view(
            template_name="users/login.html",
        ),
        name="login",
    ),
    path(
        "logout/",
        django.contrib.auth.views.LogoutView.as_view(
            template_name="users/logout.html",
        ),
        name="logout",
    )
]
