# Generated by Django 4.1.2 on 2023-05-17 14:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("events", "0005_alter_event_id"),
    ]

    operations = [
        migrations.RenameModel(old_name="Event", new_name="Events",),
    ]
