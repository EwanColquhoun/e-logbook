# Generated by Django 3.2.7 on 2021-10-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0019_auto_20211011_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
