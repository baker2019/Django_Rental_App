# Generated by Django 3.0.5 on 2020-04-09 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20200409_0528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='stay',
        ),
    ]
