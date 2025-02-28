from .models import Task
from django import forms
from django.utils.translation import gettext_lazy as _


class TaskForm(forms.Form):
    name = forms.CharField(
        label=_("Name"),
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': _('Name')}))
    description = forms.CharField(
        label=_("Description"),
        widget=forms.TextInput(attrs={
            'placeholder': _('Description')})
    )

    class Meta:
        model = Task
        fields = ['name']


class TaskDeleteForm(forms.Form):
    pass
