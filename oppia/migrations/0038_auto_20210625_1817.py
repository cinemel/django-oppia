# Generated by Django 2.2.24 on 2021-06-25 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0037_auto_20210625_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatetemplate',
            name='feedback_field',
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='quiz.Question'),
        ),
    ]
