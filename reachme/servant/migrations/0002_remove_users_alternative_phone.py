# Generated by Django 3.2 on 2021-06-07 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='alternative_phone',
        ),
    ]
