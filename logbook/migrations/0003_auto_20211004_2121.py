# Generated by Django 3.2.7 on 2021-10-04 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0002_auto_20211004_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='aircraft',
            field=models.CharField(choices=[('Boeing 747', 'Boeing 747'), ('Embraer 190', 'Embraer 190'), ('Embraer 170', 'Embraer 170'), ('Saab 2000', 'Saab 2000'), ('BAE Jetstream 41', 'BAE Jetstream 41')], default='Boeing 747', max_length=16),
        ),
        migrations.AlterField(
            model_name='flights',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
