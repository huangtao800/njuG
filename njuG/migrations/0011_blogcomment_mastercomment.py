# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0010_auto_20150721_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='masterComment',
            field=models.ForeignKey(related_name='first_blog_comment', blank=True, to='njuG.BlogComment', null=True),
        ),
    ]
