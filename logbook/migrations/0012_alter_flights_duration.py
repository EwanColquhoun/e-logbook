# Generated by Django 3.2.7 on 2021-10-09 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0011_alter_flights_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flights',
            name='duration',
            field=models.TimeField(default='01:00'),
        ),
    ]
