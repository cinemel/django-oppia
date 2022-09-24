# Generated by Django 3.2.13 on 2022-06-01 09:36

from django.db import migrations, models
import oppia.models.badges


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0048_alter_course_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatetemplate',
            name='image_file',
            field=models.ImageField(help_text='Use a .png image of 842px by 595px (at 72dpi), or use         equivalent dimension ratio for higher dpi', upload_to='certificate/templates', validators=[oppia.models.badges.CertificateTemplate.validate_image]),
        ),
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('live', 'Live'), ('draft', 'Draft'), ('archived', 'Archived'), ('new_downloads_disabled', 'New downloads disabled'), ('read_only', 'Read only')], default='live', help_text='More details about each status can be found in the <a href=https://oppiamobile.readthedocs.io/en/latest/implementers/courses/statuses.html>documentation.</a><br>Note that statuses new-downloads-disabled and read-only are only compatible with app version 7.3.9 or above.', max_length=100),
        ),
    ]
