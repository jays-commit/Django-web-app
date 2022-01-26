from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

# Meta Class gives us a nested name space for configurations and keeps it in one place
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
