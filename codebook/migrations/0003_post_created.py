# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 03:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('codebook', '0002_auto_20160607_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 7, 3, 34, 55, 631722, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
