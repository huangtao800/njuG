# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0032_auto_20150731_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='replyFrom',
            new_name='replyTo',
        ),
    ]
