# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-12 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20180521_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizattempt',
            name='ip',
            field=models.GenericIPAddressField(blank=True,
                                               default=None,
                                               null=True),
        ),
    ]
