# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0013_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
