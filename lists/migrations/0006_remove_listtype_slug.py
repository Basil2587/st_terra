# Generated by Django 3.0.5 on 2021-05-29 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20210529_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listtype',
            name='slug',
        ),
    ]
