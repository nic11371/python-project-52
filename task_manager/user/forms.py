from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import User


class UserRegisterForm(UserCreationForm):
    help_text = _('Your password must contain at least 3 characters.')
    formatted_help_text = mark_safe(f'<ul><li>{help_text}</li></ul>')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = self.formatted_help_text

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username']
