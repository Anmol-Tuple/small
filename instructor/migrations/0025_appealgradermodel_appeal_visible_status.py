# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-06-23 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0024_auto_20180623_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='appealgradermodel',
            name='appeal_visible_status',
            field=models.BooleanField(default=False),
        ),
    ]