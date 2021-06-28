# Generated by Django 3.2 on 2021-06-14 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0009_alter_complaint_subcategory_servant_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint_subcategory',
            name='servant_role',
            field=models.SmallIntegerField(choices=[(1, 'MSEB Chief Engineer'), (2, 'Health Department'), (3, 'Water Conservation officer'), (4, 'municipal corporation'), (5, 'Department Safety Officer')], default=0),
        ),
    ]