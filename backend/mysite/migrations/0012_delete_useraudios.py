# Generated by Django 4.2.8 on 2023-12-15 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_rename_textlibrary_globalaudiolibrary'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAudios',
        ),
    ]
