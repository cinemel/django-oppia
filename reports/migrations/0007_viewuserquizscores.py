# Generated by Django 3.2.13 on 2022-05-04 12:51

from django.db import migrations, models
from dbview.helpers import CreateView


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_viewusercoursecompletepercent'),
        ('profile', '0005_userprofile_exclude_from_reporting'),
        ('quiz', '0015_populate_time_taken'),
        ('oppia', '0046_course_new_downloads_enabled'),
    ]

    operations = [
        CreateView(
            name='ViewUserQuizScores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
