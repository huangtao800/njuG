# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0035_auto_20150802_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('onlyForSchool', models.BooleanField(default=True)),
                ('openToAll', models.BooleanField(default=False)),
                ('contact', models.CharField(default=b'\xe7\xa7\x81\xe4\xbf\xa1\xe6\x88\x91', max_length=20, choices=[(b'\xe7\xa7\x81\xe4\xbf\xa1\xe6\x88\x91', b'\xe7\xa7\x81\xe4\xbf\xa1\xe6\x88\x91'), (b'\xe5\xbe\xae\xe4\xbf\xa1', b'\xe5\xbe\xae\xe4\xbf\xa1')])),
                ('detailContact', models.CharField(max_length=50, null=True, blank=True)),
                ('openSchoolList', models.CharField(max_length=1000, null=True, blank=True)),
            ],
        ),
    ]
