# Generated by Django 3.2 on 2021-04-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='added_question',
            field=models.IntegerField(null=True),
        ),
    ]