from django.db import models
from django.contrib.auth.models import AbstractUser, \
    PermissionsMixin, Group, Permission, BaseUserManager
<<<<<<< HEAD
=======
from django.utils.translation import gettext as _
>>>>>>> 02d0a4a82f91e32e4ee52bd304ba6ed1b6a4fb48


class CustomUser(AbstractUser):
    first_name = models.CharField(
        max_length=100)
    last_name = models.CharField(
        max_length=100)
    username = models.CharField(
        max_length=150, unique=True)
    password1 = models.CharField(
        max_length=150)
    password2 = models.CharField(
        max_length=150)
<<<<<<< HEAD
    created_at = models.DateTimeField(auto_created=True)
=======
    created_at = models.DateTimeField(auto_now_add=True)
>>>>>>> 02d0a4a82f91e32e4ee52bd304ba6ed1b6a4fb48

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password1", "password2"]
