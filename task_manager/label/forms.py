from .models import Label
from django import forms
from django.utils.translation import gettext_lazy as _


class LabelForm(forms.Form):
    label_name = forms.CharField(
        label=_("Name"),
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': _('Name')}))

    class Meta:
        model = Label
        fields = ['label_name']


class LabelDeleteForm(forms.Form):
    pass
