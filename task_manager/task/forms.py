from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'label')
        widgets = {
            'name': forms.TextInput(attrs={
                'autofocus': 'true',
                'placeholder': _('Name')
            }),
            'description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': _('Description')
            }),
            'status': forms.Select(),
            'executor': forms.Select(),
            'labels': forms.SelectMultiple(),
        }
        label = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            'labels': _('Labels'),
        }
