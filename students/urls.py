from django.conf.urls import url, include
from views import *
urlpatterns = [
    url(r'^$', index, name="student__index"),
    url(r'^enroll/$', enroll, name="student__enroll"),
    url(r'^course/(?P<course_id>[0-9]+)/$', student_course, name="student__student_course"),
]