# Generated by Django 2.2.20 on 2021-05-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0031_auto_20210511_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='certificate_pdf',
            field=models.FileField(default=None,
                                   null=True,
                                   upload_to='certificates/%Y/%m/'),
        ),
    ]
