# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-26 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0008_auto_20180526_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeworkgroup',
            name='user',
        ),
    ]
