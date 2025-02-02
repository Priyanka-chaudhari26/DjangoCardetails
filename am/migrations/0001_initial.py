# Generated by Django 5.1.1 on 2024-09-27 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('make', models.DateField(default=datetime.date(2024, 9, 27))),
                ('model', models.CharField(max_length=100)),
                ('mileage', models.IntegerField()),
                ('engine_capacity', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=1000)),
            ],
        ),
    ]
