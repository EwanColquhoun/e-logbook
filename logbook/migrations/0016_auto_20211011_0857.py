# Generated by Django 3.2.7 on 2021-10-11 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0015_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(choices=[('7-8', '0700-0800'), ('9-10', '0900-1000'), ('11-12', '1100-1200'), ('12-14', '1300-1400'), ('14-16', '1500-1600')], default=False, max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logbook.slots'),
        ),
    ]