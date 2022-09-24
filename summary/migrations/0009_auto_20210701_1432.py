# Generated by Django 2.2.24 on 2021-07-01 14:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oppia', '0039_auto_20210627_1445'),
        ('summary', '0008_dailyactiveuser_course'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dailyactiveuser',
            unique_together={('dau', 'user', 'type', 'course')},
        ),
    ]
