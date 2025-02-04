# Generated by Django 2.2.20 on 2021-05-31 06:10

from django.db import migrations, models
import oppia.models.badges


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0032_auto_20210521_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatetemplate',
            name='image_file',
            field=models.ImageField(
                help_text='We recommend a .png image of 842px by 595px',
                upload_to='certificate/templates',
                validators=[
                    oppia.models.badges.CertificateTemplate.validate_image]),
        ),
    ]
