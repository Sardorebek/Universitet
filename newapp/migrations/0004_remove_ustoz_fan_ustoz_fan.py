# Generated by Django 4.2.6 on 2023-10-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_ustoz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ustoz',
            name='fan',
        ),
        migrations.AddField(
            model_name='ustoz',
            name='fan',
            field=models.ManyToManyField(to='newapp.fan'),
        ),
    ]
