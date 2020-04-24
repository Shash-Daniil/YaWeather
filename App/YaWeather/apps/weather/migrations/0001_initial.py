# Generated by Django 3.0.4 on 2020-04-24 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='id поста')),
                ('name', models.CharField(max_length=50, verbose_name='Имя поста')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст поста')),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 4, 24, 18, 56, 8, 436315))),
            ],
        ),
    ]
