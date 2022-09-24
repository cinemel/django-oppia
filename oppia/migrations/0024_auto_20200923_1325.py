# Generated by Django 2.2.13 on 2020-09-23 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oppia', '0023_course_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePermissions',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('role', models.CharField(choices=[('manager', 'Manager'),
                                                   ('viewer', 'Viewer')],
                                          max_length=20)),
                ('course', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='oppia.Course')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Course Permission',
                'verbose_name_plural': 'Course Permissions',
            },
        ),
        migrations.DeleteModel(
            name='CourseManager',
        ),
    ]
