# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0022_auto_20150728_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hasAvatar',
            field=models.BooleanField(default=False),
        ),
    ]
