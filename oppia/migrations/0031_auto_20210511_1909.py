# Generated by Django 2.2.20 on 2021-05-11 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0030_certificate_certificatetemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='certificate_pdf',
            field=models.FileField(default=None,
                                   null=True,
                                   upload_to='certificates'),
        ),
        migrations.AddField(
            model_name='certificatetemplate',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='certificatetemplate',
            name='image_file',
            field=models.FileField(
                help_text='We recommend a .png image of 842px by 595px',
                upload_to='certificate/templates'),
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
    ]
