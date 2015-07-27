# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('njuG', '0019_auto_20150725_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(default=b'NJU', max_length=10, choices=[(b'NJU', b'\xe5\x8d\x97\xe4\xba\xac\xe5\xa4\xa7\xe5\xad\xa6'), (b'OTHER', b'\xe5\x85\xb6\xe4\xbb\x96\xe5\xad\xa6\xe6\xa0\xa1')])),
                ('role', models.IntegerField(default=3, choices=[(0, 0), (1, 1), (2, 2), (3, 3)])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='file',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'images'),
        ),
    ]
