# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0020_auto_20150728_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='degree',
            field=models.IntegerField(default=0, choices=[(0, b'\xe6\x9c\xac\xe7\xa7\x91'), (1, b'\xe7\xa1\x95\xe5\xa3\xab'), (2, b'\xe5\x8d\x9a\xe5\xa3\xab')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='nickName',
            field=models.CharField(default=b'\xe6\x97\xa0\xe6\x98\xb5\xe7\xa7\xb0', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.IntegerField(default=3, choices=[(0, b'\xe5\x8f\x97'), (1, b'\xe6\x94\xbb'), (2, b'\xe4\xb8\x8d\xe9\x99\x90'), (3, b'-')]),
        ),
    ]
