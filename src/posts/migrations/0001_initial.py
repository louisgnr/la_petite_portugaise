# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-03-28 22:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import klingon.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('ipython', models.FileField(blank=True, null=True, upload_to='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(max_length=120)),
                ('post_comments', models.IntegerField(default=0)),
                ('big', models.BooleanField(default=False)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('image2', models.FileField(blank=True, null=True, upload_to='')),
                ('draft', models.BooleanField(default=False)),
                ('percent_read', models.ManyToManyField(blank=True, related_name='percent_read', to=settings.AUTH_USER_MODEL)),
                ('post_likes', models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL)),
                ('post_views', models.ManyToManyField(blank=True, related_name='post_views', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
            bases=(models.Model, klingon.models.Translatable),
        ),
    ]
