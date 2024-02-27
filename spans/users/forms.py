from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
import users.models


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = users.models.User
        fields = ["username", "password1", "password2"]


"""
class UserToChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = settings.AUTH_USER_MODEL
        fields = ("username", "email")


class ChangeUserProfile(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
        self.fields["coffee_count"].widget.attrs["readonly"] = True
        self.fields["coffee_count"].widget.attrs["disabled"] = True
        self.fields["coffee_count"].required = False

    class Meta:
        model = users.models.Profile
        fields = [
            users.models.Profile.birthday.field.name,
            users.models.Profile.image.field.name,
            users.models.Profile.coffee_count.field.name,
        ]
"""
