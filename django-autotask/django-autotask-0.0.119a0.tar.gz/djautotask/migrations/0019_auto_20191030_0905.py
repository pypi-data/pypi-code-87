# Generated by Django 2.1.11 on 2019-10-30 09:05

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('djautotask', '0018_auto_20191029_1634'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='resource',
            managers=[
                ('regular_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
