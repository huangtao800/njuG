# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0009_blogcomment_replyto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-time']},
        ),
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'ordering': ['-time']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-time']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-time']},
        ),
    ]
