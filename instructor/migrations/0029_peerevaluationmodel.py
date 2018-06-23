# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-06-23 10:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instructor', '0028_appealgradermodel_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeerEvaluationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peer_explanation', models.TextField()),
                ('grade', models.IntegerField(null=True)),
                ('appeal_grader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appeal_grader', to=settings.AUTH_USER_MODEL)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.CourseModel')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.HomeworkGroup', to_field='group')),
                ('peer_grader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='peer_grader', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'peer_evaluation',
            },
        ),
    ]