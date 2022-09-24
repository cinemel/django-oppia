# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-25 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('av', '0005_auto_20180424_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadedmedia',
            options={'verbose_name': 'Uploaded Media',
                     'verbose_name_plural': 'Uploaded Media'},
        ),
        migrations.AlterField(
            model_name='uploadedmediaimage',
            name='uploaded_media',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='images',
                to='av.UploadedMedia'),
        ),
    ]
