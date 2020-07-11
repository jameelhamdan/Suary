# Generated by Django 3.0.5 on 2020-07-11 09:30

import _common.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.CharField(db_column='_id', default=_common.utils.generate_uuid, max_length=36, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_blocked', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='auth.User')),
                ('following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='auth.User')),
            ],
            options={
                'db_table': 'users_follow',
                'db': 'default',
                'unique_together': {('follower', 'following')},
            },
        ),
    ]