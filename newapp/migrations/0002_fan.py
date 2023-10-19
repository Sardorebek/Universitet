# Generated by Django 4.2.6 on 2023-10-06 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
                ('asosiy', models.BooleanField(blank=True)),
                ('yonalish', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='newapp.yonalish')),
            ],
        ),
    ]