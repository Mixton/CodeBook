# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codebook', '0004_auto_20160608_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='fid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='follow',
            name='uid',
            field=models.IntegerField(),
        ),
    ]
