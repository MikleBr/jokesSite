# Generated by Django 3.1.5 on 2021-01-23 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Текст')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('likes', models.IntegerField(default='0', editable=False)),
                ('rubric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='jokes.rubric', verbose_name='Рубрика')),
            ],
            options={
                'verbose_name': 'Анекдот',
                'verbose_name_plural': 'Анекдоты',
                'ordering': ['-published'],
            },
        ),
    ]