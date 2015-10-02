# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebandit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='time',
            field=models.TimeField(default=datetime.datetime(2015, 10, 1, 15, 58, 14, 625000, tzinfo=utc)),
        ),
    ]
