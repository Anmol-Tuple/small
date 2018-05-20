# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-20 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0003_auto_20180513_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodel',
            name='no_of_student',
        ),
        migrations.AddField(
            model_name='coursehomeworkmodel',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='appeal_role',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='grading_rubric',
            field=models.TextField(null=True),
        ),
    ]
