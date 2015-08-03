# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0043_auto_20150803_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='commentCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='viewCount',
            field=models.IntegerField(default=0),
        ),
    ]
