# Generated by Django 5.0.6 on 2024-05-10 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.CharField(max_length=50, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Сенсор',
                'verbose_name_plural': 'Сенсоры',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Температура')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor')),
            ],
            options={
                'verbose_name': 'Показания',
            },
        ),
    ]
