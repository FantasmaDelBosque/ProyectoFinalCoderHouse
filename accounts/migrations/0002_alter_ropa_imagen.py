# Generated by Django 4.2.4 on 2023-10-18 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ropa',
            name='imagen',
            field=models.ImageField(upload_to='media/ropa/'),
        ),
    ]