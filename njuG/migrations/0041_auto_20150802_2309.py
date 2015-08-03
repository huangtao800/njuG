# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0040_auto_20150802_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='type',
            field=models.IntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
    ]
