# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0034_auto_20150731_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.CharField(default=b'\xe5\x8d\x97\xe4\xba\xac\xe5\xa4\xa7\xe5\xad\xa6', max_length=10, choices=[(b'\xe5\x8d\x97\xe4\xba\xac\xe5\xa4\xa7\xe5\xad\xa6', b'\xe5\x8d\x97\xe4\xba\xac\xe5\xa4\xa7\xe5\xad\xa6'), (b'\xe5\x85\xb6\xe4\xbb\x96\xe5\xad\xa6\xe6\xa0\xa1', b'\xe5\x85\xb6\xe4\xbb\x96\xe5\xad\xa6\xe6\xa0\xa1')]),
        ),
    ]
