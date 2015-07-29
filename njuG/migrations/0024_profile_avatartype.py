# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0023_profile_hasavatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatarType',
            field=models.CharField(default=b'jpg', max_length=6),
        ),
    ]
