# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cohort',
            name='course',
        ),
    ]
