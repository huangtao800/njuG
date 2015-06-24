# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0004_auto_20150624_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='replyFrom',
            field=models.ForeignKey(to='njuG.Comment', null=True),
        ),
    ]
