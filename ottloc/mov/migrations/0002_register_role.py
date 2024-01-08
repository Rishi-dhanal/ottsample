# Generated by Django 5.0.1 on 2024-01-05 07:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mov', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User'), ('child', 'Child')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]