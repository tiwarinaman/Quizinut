# Generated by Django 3.2 on 2021-04-20 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='time_duration',
            field=models.IntegerField(null=True),
        ),
    ]