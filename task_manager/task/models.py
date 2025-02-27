from django.db import models
from task_manager.status.models import Status
from task_manager.user.models import User
# from task_manager.mark.models import Mark
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    task_name = models.CharField(max_length=150, unique=True)
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
    mark = models.ManyToManyField(
        Mark,
        related_name="mark",
        blank=True,
        through='TaskRelationMark',
        verbose_name=_('Mark')
    )
    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ["task_name", "description", "status", "execute", "mark"]


class TaskRelationMark(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, on_delete=models.PROTECT)
