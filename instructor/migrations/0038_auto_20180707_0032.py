# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-07 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0037_auto_20180707_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworkgroup',
            name='grade',
            field=models.IntegerField(default=0),
        ),
    ]
