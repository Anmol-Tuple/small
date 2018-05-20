# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import UserModel

# Create your models here.


class CourseModel(models.Model):
    course_id = models.TextField()
    course_name = models.TextField()
    grading_rubric = models.TextField(null=True)
    appeal_role = models.TextField(null=True)
    instructor = models.ForeignKey(UserModel)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'course'


class CourseHomeWorkModel(models.Model):
    homework_name = models.TextField()
    grade_deadline = models.DateField()
    homework_deadline = models.DateField()
    
    # will save constraints in array form
    constraints = models.TextField()
    course = models.ForeignKey(CourseModel)
    attachment = models.TextField(null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'course_homework'

class StudentCourseEnrolledModel(models.Model):
    course = models.ForeignKey(CourseModel)
    student = models.TextField()

    class Meta:
        db_table = 'course_student'