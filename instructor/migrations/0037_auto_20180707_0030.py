# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-07 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0036_auto_20180703_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursehomeworkmodel',
            name='no_of_grader',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coursehomeworkmodel',
            name='no_of_group',
            field=models.IntegerField(null=True),
        ),
    ]
