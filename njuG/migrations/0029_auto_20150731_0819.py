# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('njuG', '0028_profile_unreadmessagecount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='masterBlog',
        ),
        migrations.RemoveField(
            model_name='message',
            name='masterPost',
        ),
        migrations.RemoveField(
            model_name='message',
            name='source',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
