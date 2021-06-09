# Generated by Django 3.1 on 2021-01-19 12:08

from datetime import timedelta

import auth_token.enums
import auth_token.models
from django.conf import settings
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth_token', '0010_auto_20190723_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorizationToken',
            fields=[
                ('created_at', models.DateTimeField(db_index=True, verbose_name='created at')),
                ('changed_at', models.DateTimeField(db_index=True, verbose_name='changed at')),
                ('key', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='key')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('user_agent', models.CharField(blank=True, max_length=256, null=True, verbose_name='user agent')),
                ('expires_at', models.DateTimeField(default=auth_token.models.compute_authorization_token_expires_at,
                                                    verbose_name='expires at')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('auth_slug', models.SlugField(blank=True, null=True, verbose_name='slug')),
                ('backend', models.CharField(max_length=250, verbose_name='backend')),
                ('allowed_cookie', models.BooleanField(default=True, verbose_name='is allowed cookie')),
                ('allowed_header', models.BooleanField(default=True, verbose_name='is allowed header')),
                ('is_authenticated', models.BooleanField(default=False, verbose_name='is authenticated')),
                ('preserve_cookie', models.BooleanField(default=False, verbose_name='preserve cookie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='authorization_tokens',
                                           to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'authorization token',
                'verbose_name_plural': 'authorization tokens',
            },
        ),
        migrations.CreateModel(
            name='AuthorizationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='slug')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('result',
                 enumfields.fields.NumEnumField(blank=True, enum=auth_token.enums.AuthorizationRequestResult, null=True,
                                                verbose_name='result')),
                ('backend', models.CharField(max_length=250, verbose_name='backend')),
                ('data', models.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True,
                                          verbose_name='data')),
                ('expires_at', models.DateTimeField(blank=True, null=True, verbose_name='expires at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='authorization_requests',
                                           to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('granted_at', models.DateTimeField(null=True, blank=True, verbose_name='granted at')),
            ],
            options={
                'verbose_name': 'authorization request',
                'verbose_name_plural': 'authorization requests',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='AuthorizationRequestGenericManyToManyRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at')),
                ('object_id', models.TextField(db_index=True, verbose_name='ID of the related object')),
                ('authorization_request',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_related_objects',
                                   related_query_name='related_objects', to='auth_token.authorizationrequest')),
                ('object_ct',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype',
                                   verbose_name='content type of the related object')),
            ],
            options={
                'db_tablespace': '',
                'unique_together': {('authorization_request', 'object_ct', 'object_id')},
            },
        ),
        migrations.CreateModel(
            name='AuthorizationTokenGenericManyToManyRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at')),
                ('object_id', models.TextField(db_index=True, verbose_name='ID of the related object')),
                ('authorization_token',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_related_objects',
                                   related_query_name='related_objects', to='auth_token.authorizationtoken')),
                ('object_ct',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype',
                                   verbose_name='content type of the related object')),
            ],
            options={
                'db_tablespace': '',
                'unique_together': {('authorization_token', 'object_ct', 'object_id')},
            },
        ),
        migrations.RenameModel('DeviceKey', 'MobileDevice'),
        migrations.CreateModel(
            name='OneTimePassword',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at')),
                ('key', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='key')),
                ('expires_at', models.DateTimeField(blank=True, null=True, verbose_name='expires at')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('data', models.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True,
                                          verbose_name='data')),
            ],
            options={
                'verbose_name': 'one time password',
                'verbose_name_plural': 'one time passwords',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='OneTimePasswordGenericManyToManyRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at')),
                ('object_id', models.TextField(db_index=True, verbose_name='ID of the related object')),
                ('object_ct',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype',
                                   verbose_name='content type of the related object')),
                ('one_time_password',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_related_objects',
                                   related_query_name='related_objects', to='auth_token.onetimepassword')),
            ],
            options={
                'db_tablespace': '',
                'unique_together': {('one_time_password', 'object_ct', 'object_id')},
            },
        ),
        migrations.CreateModel(
            name='UserAuthorizationTokenTakeover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='changed at')),
                ('is_active', models.BooleanField()),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_takeovers',
                                            to='auth_token.authorizationtoken', verbose_name='authorization token')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_token_takeovers',
                                   to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'authorization takeover',
                'verbose_name_plural': 'authorization takeovers',
            },
        ),
        migrations.AddField(
            model_name='authorizationrequest',
            name='authorization_token',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='authorization_requests', to='auth_token.authorizationtoken',
                                    verbose_name='authorization token'),
        ),
        migrations.AddField(
            model_name='mobiledevice',
            name='changed_at',
            field=models.DateTimeField(null=True, blank=True, db_index=True, verbose_name='changed at'),
        ),
        migrations.AddField(
            model_name='mobiledevice',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='mobiledevice',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='mobiledevice',
            name='is_primary',
            field=models.BooleanField(default=False, verbose_name='is primary'),
        ),
        migrations.AlterField(
            model_name='mobiledevice',
            name='uuid',
            field=models.CharField(max_length=36, verbose_name='UUID'),
        ),
        migrations.AlterField(
            model_name='mobiledevice',
            name='user',
            field=models.ForeignKey(
                to=settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
                verbose_name='user',
                related_name='mobile_devices'
            )
        ),
        migrations.AddField(
            model_name='authorizationtoken',
            name='mobile_device',
            field=models.ForeignKey(
                verbose_name='mobile device',
                to='auth_token.mobiledevice',
                related_name='authorization_tokens',
                null=True,
                blank=True,
                on_delete=models.CASCADE
            ),
        ),
    ]
