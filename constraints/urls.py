from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from views import index
urlpatterns = [
    url(r'$', index)
]
