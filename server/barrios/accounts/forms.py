from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import Form, CharField, PasswordInput

from .models import CustomUser


class LoginForm(Form):
    username = CharField(max_length=65, required=True)
    password = CharField(max_length=65, required=True, widget=PasswordInput)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")
