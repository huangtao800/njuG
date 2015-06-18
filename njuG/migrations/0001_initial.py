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
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField(auto_now=True)),
                ('content', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField(auto_now=True)),
                ('content', models.CharField(max_length=300)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='njuG.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='replyFrom',
            field=models.ForeignKey(to='njuG.Comment', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
