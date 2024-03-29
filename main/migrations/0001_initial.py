# Generated by Django 3.0.5 on 2020-07-11 09:30

import _common.utils
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(default=_common.utils.generate_uuid, max_length=36, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='auth.User')),
            ],
            options={
                'db_table': 'main_comments',
                'db': 'default',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(default=_common.utils.generate_uuid, max_length=36, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='auth.User')),
            ],
            options={
                'db_table': 'main_posts',
                'db': 'default',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.TextField(db_index=True)),
                ('content_type', models.TextField(db_index=True)),
                ('comment', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media', to='main.Comment')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='media', to='main.Post')),
            ],
            options={
                'db_table': 'main_media',
                'db': 'default',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.CharField(default=_common.utils.generate_uuid, max_length=36, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='main.Comment')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='auth.User')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='main.Post')),
            ],
            options={
                'db_table': 'main_likes',
                'db': 'default',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.Post'),
        ),
    ]
