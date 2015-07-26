# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('njuG', '0018_auto_20150725_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(upload_to=b'images')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
