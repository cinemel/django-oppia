# Generated by Django 2.2.27 on 2022-03-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0010_auto_20210816_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercoursesummary',
            name='total_activity_current',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='usercoursesummary',
            name='total_activity_previous',
            field=models.IntegerField(default=0),
        ),
    ]
