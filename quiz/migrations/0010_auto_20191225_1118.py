# Generated by Django 2.2.8 on 2019-12-25 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20190321_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizattemptresponse',
            name='quizattempt',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='responses',
                to='quiz.QuizAttempt'),
        ),
    ]
