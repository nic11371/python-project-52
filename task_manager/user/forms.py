from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms
from django.utils.translation import gettext as _


class UserForm(UserCreationForm):
    first_name = forms.CharField(
        label="First name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Name')}))
    last_name = forms.CharField(
        label="Last name",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Last name')}))
    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Username')}),
        help_text="id_username",
        required=True)
    password1 = forms.CharField(
        label="Password",
        min_length=3,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Password'),
            'autocomplete': 'new-password'}),
        help_text="id_password1",
        required=True)
    password2 = forms.CharField(
        label="Confirm password",
        min_length=3,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Password'),
            'autocomplete': 'new-password'}),
        help_text="id_password2",
        required=True)

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Username'),
            'autocapitalize': 'none',
            'autocomplete': 'username'}),
        help_text="id_username",
        required=True)
    password = forms.CharField(
        label="Password",
        min_length=3,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Password'),
            'autocomplete': 'current-password'}),
        required=True)
