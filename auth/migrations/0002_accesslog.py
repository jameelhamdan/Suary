# Generated by Django 3.0.3 on 2020-03-03 17:58

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
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