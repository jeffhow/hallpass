# Generated by Django 4.2.16 on 2024-09-09 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passes', '0022_rename_graduation_year_student_yog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='yog',
            field=models.IntegerField(default=2024),
        ),
    ]
