# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0042_message_mastercomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.CharField(default='\u5357\u4eac\u5927\u5b66', max_length=10, choices=[('\u5357\u4eac\u5927\u5b66', '\u5357\u4eac\u5927\u5b66'), ('\u6cb3\u6d77\u5927\u5b66', '\u6cb3\u6d77\u5927\u5b66'), ('\u4e1c\u5357\u5927\u5b66', '\u4e1c\u5357\u5927\u5b66'), ('\u5176\u4ed6\u5b66\u6821', '\u5176\u4ed6\u5b66\u6821')]),
        ),
    ]
