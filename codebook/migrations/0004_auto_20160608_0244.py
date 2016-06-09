# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 02:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codebook', '0003_post_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='fid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follow',
            name='uid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]
