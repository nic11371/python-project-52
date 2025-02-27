from django.db import models
from django.utils.translation import gettext as _


class Label(models.Model):
    label_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ["label_name"]
