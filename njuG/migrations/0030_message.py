# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('njuG', '0029_auto_20150731_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('isRead', models.BooleanField(default=False)),
                ('type', models.IntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('content', models.TextField()),
                ('masterBlog', models.ForeignKey(blank=True, to='njuG.Blog', null=True)),
                ('masterPost', models.ForeignKey(blank=True, to='njuG.Post', null=True)),
                ('source', models.ForeignKey(related_name='source', to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(related_name='target', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
