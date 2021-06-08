# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-06-03 02:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import leprikon.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("leprikon", "0060_transactions"),
    ]

    operations = [
        migrations.CreateModel(
            name="RefundRequest",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "requested",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False, verbose_name="requested time"
                    ),
                ),
                ("bank_account", leprikon.models.fields.BankAccountField(verbose_name="bank account number")),
                (
                    "registration",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="refund_request",
                        to="leprikon.SubjectRegistration",
                        verbose_name="registration",
                    ),
                ),
                (
                    "requested_by",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="requested by",
                    ),
                ),
            ],
            options={
                "verbose_name": "refund request",
                "verbose_name_plural": "refund requests",
                "ordering": ("requested",),
            },
        ),
    ]
