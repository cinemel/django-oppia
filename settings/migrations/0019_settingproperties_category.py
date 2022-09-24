# Generated by Django 2.2.24 on 2021-07-16 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0018_email_certificate_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingproperties',
            name='category',
            field=models.CharField(blank=True, choices=[
                ('system', 'System'),
                ('gamification', 'Gamification'),
                ('system_config', 'System configuration'),
                ('certification', 'Certification'),
                ('analytics', 'Analytics'),
                ('visualisations', 'Visualisations'),
                ('app', 'App'),
                ('server_registration', 'Server Registration')],
                default='system', max_length=50, null=True),
        ),
    ]
