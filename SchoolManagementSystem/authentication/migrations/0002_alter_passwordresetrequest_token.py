# Generated by Django 5.1.4 on 2024-12-06 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetrequest',
            name='token',
            field=models.CharField(default='t7RijJKgu2vkts4lD8ydZRVbDwC3x2LW', editable=False, max_length=32, unique=True),
        ),
    ]
