# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-22 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0018_groupcombinationmodel_is_used'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeworkgroup',
            name='appeal_canceled',
            field=models.BooleanField(default=False),
        ),
    ]
