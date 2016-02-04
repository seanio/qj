# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('queuejumper', '0002_auto_20160129_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='queue',
            field=models.ForeignKey(to='queuejumper.Queue'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time_placed',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 29, 4, 31, 18, 760694, tzinfo=utc)),
        ),
    ]
