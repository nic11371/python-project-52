from django import forms
from django.contrib.auth.forms import (
    PasswordChangeForm,
    UserChangeForm,
    UserCreationForm,
)
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import User


class UserRegisterForm(UserCreationForm):
    help_text = _(
            'Your password must contain at least 3 characters.')
    formatted_help_text = mark_safe(f'<ul><li>{help_text}</li></ul>')

    first_name = forms.CharField(
        label=_("First name"),
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': _('Name')}))
    last_name = forms.CharField(
        label=_("Last name"),
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': _('Last name')}))
    username = forms.CharField(
        label=_("Username"),
        max_length=150,
        help_text=_(
            '''Required field. No more than 150 characters. 
                    Only letters, numbers and symbols @/./+/-/_.'''),
        widget=forms.TextInput(attrs={
            'placeholder': _('Username'), }),
        required=True)
    password1 = forms.CharField(
        label=_("Password"),
        min_length=3,
        help_text=formatted_help_text,
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Password'),
            'autocomplete': 'new-password'}),
        required=True)
    password2 = forms.CharField(
        label=_("Confirm password"),
        min_length=3,
        help_text=_('To confirm, please enter your password again.'),
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Password'),
            'autocomplete': 'new-password'}),
        required=True)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    first_name = forms.CharField(
        label=_("First name"),
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': _('Name')}))
    last_name = forms.CharField(
        label=_("Last name"),
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': _('Last name')}))
    username = forms.CharField(
        label=_("Username"),
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': _('Username')}),
        required=True)
    password = None

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username']


class UserPasswordChange(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        min_length=3,
        widget=forms.PasswordInput(attrs={
            'placeholder': _('New password'),
            'autocomplete': 'new-password'}),
        required=True)
    new_password2 = forms.CharField(
        label=_("Confirm new password"),
        min_length=3,
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Confirm password'),
            'autocomplete': 'new-password'}),
        required=True)
    old_password = forms.CharField(
        label=_("Old password"),
        min_length=3,
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Old password'),
            'autocomplete': 'new-password'}),
        required=True)

    class Meta:
        model = User
        fields = ['passsword1', 'password2']


class UserDeleteForm(forms.Form):
    pass
