# Generated by Django 4.2.4 on 2023-08-02 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passes', '0004_destination_thing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='thing',
        ),
    ]