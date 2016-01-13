# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('album_name', models.CharField(max_length=30)),
                ('album_description', models.CharField(max_length=200)),
                ('album_date', models.DateTimeField()),
                ('album_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'album',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('photo_name', models.CharField(max_length=20)),
                ('photo_description', models.CharField(max_length=100)),
                ('photo_date', models.DateTimeField()),
                ('photo_image', models.ImageField(upload_to='images/')),
                ('photo_album', models.ForeignKey(to='un.Album')),
                ('photo_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'photo',
            },
        ),
    ]
