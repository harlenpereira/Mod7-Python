# Generated by Django 4.0.6 on 2022-11-24 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetoDjango2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('data', models.DateTimeField(default=datetime.datetime(2022, 11, 24, 9, 52, 6, 759374), verbose_name='Publicado em')),
            ],
        ),
    ]
