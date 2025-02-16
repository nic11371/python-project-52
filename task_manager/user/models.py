from django.db import models


class User(models.Model):
    nic_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
