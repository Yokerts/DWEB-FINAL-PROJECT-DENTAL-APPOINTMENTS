from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class UserUpdateForm(UserChangeForm):
    password = None  # oculta el campo password

    class Meta:
        model = User
        fields = ["username", "email"]
