# Generated by Django 2.0.1 on 2018-01-14 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shorty', '0004_auto_20180114_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skrcurl',
            name='active',
        ),
        migrations.RemoveField(
            model_name='skrcurl',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='skrcurl',
            name='updated',
        ),
    ]
