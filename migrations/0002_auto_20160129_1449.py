# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('queuejumper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='priority',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='order',
            name='time_placed',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 29, 3, 49, 27, 786977, tzinfo=utc)),
        ),
    ]
