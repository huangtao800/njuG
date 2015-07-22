# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0011_blogcomment_mastercomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='content',
            field=models.TextField(),
        ),
    ]
