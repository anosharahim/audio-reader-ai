# Generated by Django 4.2.5 on 2023-10-14 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_textlibrary_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textlibrary',
            name='website_url',
            field=models.URLField(unique=True),
        ),
    ]
