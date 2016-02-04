# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('queuejumper', '0004_auto_20160130_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(to='queuejumper.Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time_placed',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 30, 10, 18, 27, 243456, tzinfo=utc)),
        ),
    ]
