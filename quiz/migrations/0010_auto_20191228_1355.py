# Generated by Django 2.2.8 on 2019-12-28 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20190321_0755'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizattempt',
            options={'ordering': ['-submitted_date', '-attempt_date'],
                     'verbose_name': 'QuizAttempt',
                     'verbose_name_plural': 'QuizAttempts'},
        ),
        migrations.AlterField(
            model_name='quizattemptresponse',
            name='quizattempt',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='responses',
                to='quiz.QuizAttempt'),
        ),
    ]
