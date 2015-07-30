# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0025_auto_20150730_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='like',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
