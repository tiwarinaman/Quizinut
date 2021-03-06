# Generated by Django 3.2 on 2021-04-20 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_quiz_time_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('marks', models.PositiveIntegerField(null=True)),
                ('option1', models.CharField(max_length=300)),
                ('option2', models.CharField(max_length=300)),
                ('option3', models.CharField(max_length=300)),
                ('option4', models.CharField(max_length=300)),
                ('correct_answer', models.CharField(max_length=300)),
                ('quiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.teacher')),
            ],
        ),
    ]
