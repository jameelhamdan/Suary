# Generated by Django 3.0.5 on 2020-07-11 09:30

import _common.utils
import _common.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(db_index=True, default=_common.utils.generate_uuid, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('username', models.CharField(db_index=True, editable=False, max_length=128, unique=True, validators=[_common.validators.UsernameValidator])),
                ('email', models.EmailField(db_index=True, max_length=128, unique=True)),
                ('avatar_uuid', models.CharField(max_length=36, null=True)),
                ('password_hash', models.CharField(max_length=512)),
                ('secret_key', models.CharField(db_index=True, default='', max_length=108)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=256)),
                ('birth_date', models.DateField()),
            ],
            options={
                'db': 'default',
            },
        ),
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('login', 'Login'), ('register', 'Register'), ('fail', 'Login Failed'), ('logout_all', 'Logout all sessions'), ('Forbidden', 'Forbidden')], default='login', max_length=16)),
                ('ip', models.GenericIPAddressField(db_index=True, null=True)),
                ('agent', models.CharField(max_length=128, null=True)),
                ('http_accept', models.CharField(max_length=1025)),
                ('path_info', models.CharField(max_length=255)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db': 'default',
            },
        ),
    ]
