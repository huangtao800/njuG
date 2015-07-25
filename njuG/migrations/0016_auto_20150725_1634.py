# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0015_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img1',
            field=models.ForeignKey(related_name='img1', blank=True, to='njuG.Image', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='img2',
            field=models.ForeignKey(related_name='img2', blank=True, to='njuG.Image', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='img3',
            field=models.ForeignKey(related_name='img3', blank=True, to='njuG.Image', null=True),
        ),
    ]
