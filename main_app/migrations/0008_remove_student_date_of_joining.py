# Generated by Django 5.1.4 on 2024-12-12 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_student_date_of_joining'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_of_joining',
        ),
    ]
