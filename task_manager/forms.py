from django.contrib.auth.forms import AuthenticationForm
from .user.models import CustomUser
from django import forms
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Username"),
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': _('Username'),
            'autocapitalize': 'none',
            'autocomplete': 'username'}),
        required=True)
    password = forms.CharField(
        label=_("Password"),
        min_length=3,
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Password'),
            'autocomplete': 'current-password'}),
        required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']
