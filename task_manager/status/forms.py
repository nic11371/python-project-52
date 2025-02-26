from .models import Status
from django import forms
from django.utils.translation import gettext_lazy as _


class StatusForm(forms.Form):
    status_name = forms.CharField(
        label=_("Name"),
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': _('Name')}))

    class Meta:
        model = Status
        fields = ['status_name']


class StatusDeleteForm(forms.Form):
    pass
