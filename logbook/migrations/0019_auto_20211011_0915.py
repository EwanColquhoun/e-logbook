# Generated by Django 3.2.7 on 2021-10-11 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logbook', '0018_auto_20211011_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='slot',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='slot_booking', to='logbook.slots'),
        ),
    ]
