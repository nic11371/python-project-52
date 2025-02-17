from django.forms import ModelForm
from .models import User
from django import forms


class UserForm(ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=150, required=True)
    password1 = forms.CharField(min_length=3)
    password2 = forms.CharField(min_length=3)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'password1', 'password2']


class LoginForm(ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(min_length=3)

    class Meta:
        model = User
        fields = ['username', 'password']
