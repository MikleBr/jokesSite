# Generated by Django 3.1.5 on 2021-01-23 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joke',
            name='rubric',
        ),
        migrations.AddField(
            model_name='joke',
            name='rubric',
            field=models.ManyToManyField(to='jokes.Rubric'),
        ),
    ]
