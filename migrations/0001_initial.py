# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('username', models.CharField(primary_key=True, serialize=False, max_length=200)),
                ('maxjumps', models.IntegerField(default=0)),
                ('balance', models.FloatField(default=0)),
                ('credit', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('priority', models.IntegerField()),
                ('time_placed', models.DateTimeField()),
                ('filled', models.BooleanField(default=False)),
                ('been_jumped', models.IntegerField(default=0)),
                ('has_jumped', models.IntegerField(default=0)),
                ('details', models.CharField(max_length=300)),
                ('customer', models.OneToOneField(to='queuejumper.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('store_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='queue',
            field=models.OneToOneField(to='queuejumper.Queue'),
        ),
    ]
