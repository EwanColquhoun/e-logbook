# Generated by Django 3.2.7 on 2021-10-11 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0020_booking_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
