# Generated by Django 4.2.4 on 2023-08-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='thing',
            field=models.CharField(default='', max_length=200),
        ),
    ]