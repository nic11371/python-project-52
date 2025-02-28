from django.db import models
from task_manager.status.models import Status
from task_manager.user.models import User
from task_manager.label.models import Label
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        null=True,
        verbose_name=_('Status')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name=_('Author')
    )
    execute = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='execute',
        verbose_name=_('Execute')
    )
    label = models.ManyToManyField(
        Label,
        related_name="label",
        blank=True,
        through='TaskRelationLabel',
        verbose_name=_('Label')
    )
    created_at = models.DateTimeField(auto_now_add=True)


class TaskRelationLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
