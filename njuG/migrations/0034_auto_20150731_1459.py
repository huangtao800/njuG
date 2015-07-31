# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0033_auto_20150731_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='blogComment',
            field=models.ForeignKey(blank=True, to='njuG.BlogComment', null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='postComment',
            field=models.ForeignKey(blank=True, to='njuG.Comment', null=True),
        ),
    ]
