# Generated by Django 4.2.4 on 2023-10-19 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
