# Generated by Django 3.2 on 2021-04-22 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20210422_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='number_of_attempts',
            field=models.IntegerField(default=0, null=True),
        ),
    ]