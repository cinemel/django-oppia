# Generated by Django 2.2.13 on 2020-11-08 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('summary', '0005_auto_20201107_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyActiveUser',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('type', models.CharField(choices=[('submitted', 'submitted'),
                                                   ('tracker', 'tracker')],
                                          max_length=20)),
                ('dau', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='summary.DailyActiveUsers')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'DailyActiveUser',
                'verbose_name_plural': 'DailyActiveUsers',
                'unique_together': {('dau', 'user', 'type')},
            },
        ),
    ]
