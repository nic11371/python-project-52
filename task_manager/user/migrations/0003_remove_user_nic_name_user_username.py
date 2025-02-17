# Generated by Django 4.2.11 on 2025-02-17 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_nic_user_nic_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nic_name',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
