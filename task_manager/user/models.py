from django.db import models
from django.contrib.auth.models import AbstractUser, \
    PermissionsMixin, Group, Permission, BaseUserManager
from django.utils.translation import gettext as _


class User(AbstractUser):
    password1 = models.CharField(
        max_length=150)
    password2 = models.CharField(
        max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password1", "password2"]
