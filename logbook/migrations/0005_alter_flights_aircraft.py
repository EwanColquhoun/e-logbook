# Generated by Django 3.2.7 on 2021-10-05 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0004_alter_flights_aircraft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flights',
            name='aircraft',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
