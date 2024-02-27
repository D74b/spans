import django
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError("Users must have a username.")
        # if email is None:
        #    raise TypeError("Users must have an email address.")

        user = self.model(
            username=username,
            # email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    def get_userfiles_path(self, filename):
        return f"users/{self.username}/{filename}"

    objects = UserManager()

    username = django.db.models.CharField(
        db_index=True,
        max_length=255,
        unique=True,
    )

    USERNAME_FIELD = 'username'

    email = django.db.models.EmailField(db_index=True, unique=True, null=True, blank=True)

    is_active = django.db.models.BooleanField(default=True)

    is_staff = django.db.models.BooleanField(default=False)

    is_superuser = django.db.models.BooleanField(default=False)

    created_at = django.db.models.DateTimeField(auto_now_add=True)

    image = django.db.models.ImageField(
        "фото профиля",
        upload_to=get_userfiles_path,
        help_text="Фото пользователя",
        null=True,
        blank=True,
    )
