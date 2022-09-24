# Generated by Django 3.2.13 on 2022-08-08 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0053_auto_20220803_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='cohort',
            name='criteria_based',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cohort',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='CohortCritera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student')], default='student', max_length=20)),
                ('user_profile_field', models.CharField(max_length=150)),
                ('user_profile_value', models.TextField()),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oppia.cohort')),
            ],
            options={
                'verbose_name': 'Cohort criteria',
            },
        ),
    ]