# Generated by Django 4.2.8 on 2023-12-15 16:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0012_delete_useraudios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GlobalAudioLibrary',
            new_name='AudioItem',
        ),
    ]