# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0047_auto_20160107_1427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['isRead', '-time']},
        ),
    ]
