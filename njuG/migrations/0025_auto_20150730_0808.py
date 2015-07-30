# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0024_profile_avatartype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='degree',
            field=models.CharField(default=b'\xe6\x9c\xac\xe7\xa7\x91', max_length=3, choices=[(b'\xe6\x9c\xac\xe7\xa7\x91', b'\xe6\x9c\xac\xe7\xa7\x91'), (b'\xe7\xa1\x95\xe5\xa3\xab', b'\xe7\xa1\x95\xe5\xa3\xab'), (b'\xe5\x8d\x9a\xe5\xa3\xab', b'\xe5\x8d\x9a\xe5\xa3\xab')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(default=b'\xe4\xbf\x9d\xe5\xaf\x86', max_length=5, choices=[(b'\xe5\x8f\x97', b'\xe5\x8f\x97'), (b'\xe6\x94\xbb', b'\xe6\x94\xbb'), (b'\xe4\xb8\x8d\xe9\x99\x90', b'\xe4\xb8\x8d\xe9\x99\x90'), (b'\xe4\xbf\x9d\xe5\xaf\x86', b'-')]),
        ),
    ]
