# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-16 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_quizattempt_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizattempt',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='quizattempt',
            name='instance_id',
            field=models.CharField(blank=True,
                                   db_index=True,
                                   default=None,
                                   max_length=100,
                                   null=True),
        ),
    ]
