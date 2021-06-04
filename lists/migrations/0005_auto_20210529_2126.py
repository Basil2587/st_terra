# Generated by Django 3.0.5 on 2021-05-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_mylist_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mylist',
            name='slug',
        ),
        migrations.AddField(
            model_name='listtype',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]