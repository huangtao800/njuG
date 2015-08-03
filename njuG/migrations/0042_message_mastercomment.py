# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0041_auto_20150802_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='masterComment',
            field=models.ForeignKey(related_name='master_comment', blank=True, to='njuG.BlogComment', null=True),
        ),
    ]
