# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0039_auto_20150802_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='contact',
            field=models.CharField(default='\u79c1\u4fe1\u6211', max_length=20, choices=[('\u79c1\u4fe1\u6211', '\u79c1\u4fe1\u6211'), ('\u5fae\u4fe1', '\u5fae\u4fe1')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='degree',
            field=models.CharField(default='\u672c\u79d1', max_length=3, choices=[('\u672c\u79d1', '\u672c\u79d1'), ('\u7855\u58eb', '\u7855\u58eb'), ('\u535a\u58eb', '\u535a\u58eb')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(default='\u4fdd\u5bc6', max_length=5, choices=[('\u53d7', '\u53d7'), ('\u653b', '\u653b'), ('\u4e0d\u9650', '\u4e0d\u9650'), ('\u4fdd\u5bc6', b'-')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.CharField(default='\u5357\u4eac\u5927\u5b66', max_length=10, choices=[('\u5357\u4eac\u5927\u5b66', '\u5357\u4eac\u5927\u5b66'), ('\u5176\u4ed6\u5b66\u6821', '\u5176\u4ed6\u5b66\u6821')]),
        ),
    ]
