# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-09 17:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0015_tracker_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityschedule',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='course',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='cohort',
            name='schedule',
        ),
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ActivitySchedule',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
