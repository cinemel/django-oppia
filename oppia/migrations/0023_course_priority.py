# Generated by Django 2.2.10 on 2020-05-07 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0022_auto_20200224_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]
