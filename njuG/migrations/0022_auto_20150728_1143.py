# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0021_auto_20150728_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.IntegerField(default=4, choices=[(2, b'\xe5\x8f\x97'), (1, b'\xe6\x94\xbb'), (3, b'\xe4\xb8\x8d\xe9\x99\x90'), (4, b'-')]),
        ),
    ]
