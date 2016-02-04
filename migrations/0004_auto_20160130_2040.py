# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('queuejumper', '0003_auto_20160129_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cancelled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='time_placed',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 30, 9, 40, 3, 340251, tzinfo=utc)),
        ),
    ]
