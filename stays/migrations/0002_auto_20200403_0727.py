# Generated by Django 3.0.5 on 2020-04-03 07:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20200403_0727'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stays', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stays',
            new_name='Stay',
        ),
    ]
