from django.db import models
from django.utils.translation import gettext as _


class Status(models.Model):
    status_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ["status_name"]
