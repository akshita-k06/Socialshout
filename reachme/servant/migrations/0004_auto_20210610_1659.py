# Generated by Django 3.2 on 2021-06-10 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servant', '0003_alter_users_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='otp_code',
        ),
        migrations.RemoveField(
            model_name='users',
            name='otp_created_at',
        ),
    ]
