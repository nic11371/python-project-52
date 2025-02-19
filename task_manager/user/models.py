from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class CustomUser(AbstractUser):
    created_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.username
