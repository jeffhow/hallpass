# Generated by Django 4.2.16 on 2024-09-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passes', '0020_alter_profile_queue'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='graduation_year',
            field=models.IntegerField(default=2024),
            preserve_default=False,
        ),
    ]