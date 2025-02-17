from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150)
    full_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(null=True)
