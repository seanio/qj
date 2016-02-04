# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('queuejumper', '0005_auto_20160130_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_placed',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 6, 24, 23, 471376, tzinfo=utc)),
        ),
    ]
