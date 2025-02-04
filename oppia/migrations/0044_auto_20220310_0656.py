# Generated by Django 2.2.27 on 2022-03-10 06:56

from django.db import migrations, models
import oppia.models.badges


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0043_auto_20220210_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatetemplate',
            name='image_file',
            field=models.ImageField(
                help_text='Use a .png image of 842px by 595px (at 72dpi), or use equivalent dimension ratio for higher '
                          'dpi',
                upload_to='certificate/templates',
                validators=[oppia.models.badges.CertificateTemplate.validate_image]),
        ),
    ]
