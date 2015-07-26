# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0017_delete_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='img3',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
