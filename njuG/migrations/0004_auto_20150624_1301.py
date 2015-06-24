# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0003_auto_20150624_1012'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('user', 'post')]),
        ),
    ]
