# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0027_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='unreadMessageCount',
            field=models.IntegerField(default=0),
        ),
    ]
