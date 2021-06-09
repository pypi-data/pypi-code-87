# Generated by Django 3.1 on 2021-01-19 12:08

from datetime import timedelta

from django.conf import settings
from django.db import migrations, models
from django.db.models import F


def set_mobile_device_changed_at(apps, schema_editor):
    MobileDevice = apps.get_model('auth_token', 'MobileDevice')
    MobileDevice.objects.filter(last_login__isnull=True).update(changed_at=F('created_at'))
    MobileDevice.objects.filter(last_login__isnull=False).update(changed_at=F('last_login'))


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth_token', '0011_auto_20210119_1308'),
    ]

    operations = [
        migrations.RunPython(set_mobile_device_changed_at),
    ]
