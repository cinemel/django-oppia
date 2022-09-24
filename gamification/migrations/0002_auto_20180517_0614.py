# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-17 06:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    STR_DATE_CREATED = b'date created'

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0005_auto_20180416_1318'),
        ('oppia', '0013_auto_20180413_1611'),
        ('gamification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityGamificationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('created_date',
                 models.DateTimeField(default=django.utils.timezone.now,
                                      verbose_name=STR_DATE_CREATED)),
                ('event', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
                ('activity',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='oppia.Activity')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activity Gamification Event',
                'verbose_name_plural': 'Activity Gamification Events',
            },
        ),
        migrations.CreateModel(
            name='CourseGamificationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('created_date',
                 models.DateTimeField(default=django.utils.timezone.now,
                                      verbose_name=STR_DATE_CREATED)),
                ('event', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
                ('course',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='oppia.Course')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Course Gamification Event',
                'verbose_name_plural': 'Course Gamification Events',
            },
        ),
        migrations.CreateModel(
            name='MediaGamificationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('created_date',
                 models.DateTimeField(default=django.utils.timezone.now,
                                      verbose_name=STR_DATE_CREATED)),
                ('event', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
                ('media',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='oppia.Media')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Media Gamification Event',
                'verbose_name_plural': 'Media Gamification Events',
            },
        ),
        migrations.CreateModel(
            name='QuizGamificationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('created_date',
                 models.DateTimeField(default=django.utils.timezone.now,
                                      verbose_name=STR_DATE_CREATED)),
                ('event', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
                ('quiz',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='quiz.Quiz')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quiz Gamification Event',
                'verbose_name_plural': 'Quiz Gamification Events',
            },
        ),
        migrations.RemoveField(
            model_name='activitygamificationpoints',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='activitygamificationpoints',
            name='user',
        ),
        migrations.RemoveField(
            model_name='coursegamificationpoints',
            name='course',
        ),
        migrations.RemoveField(
            model_name='coursegamificationpoints',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mediagamificationpoints',
            name='media',
        ),
        migrations.RemoveField(
            model_name='mediagamificationpoints',
            name='user',
        ),
        migrations.RemoveField(
            model_name='quizgamificationpoints',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quizgamificationpoints',
            name='user',
        ),
        migrations.DeleteModel(
            name='ActivityGamificationPoints',
        ),
        migrations.DeleteModel(
            name='CourseGamificationPoints',
        ),
        migrations.DeleteModel(
            name='MediaGamificationPoints',
        ),
        migrations.DeleteModel(
            name='QuizGamificationPoints',
        ),
    ]
