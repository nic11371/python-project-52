from django.forms import ModelForm
from .models import User
from django import forms


class UserForm(ModelForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    nic_name = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True)
    conf_password = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'nic_name', 'password', 'conf_password']
