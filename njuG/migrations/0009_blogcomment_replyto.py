# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0008_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='replyTo',
            field=models.ForeignKey(blank=True, to='njuG.BlogComment', null=True),
        ),
    ]
