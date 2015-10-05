__author__ = 'siyu'
from django.conf.urls import include, url
from django.contrib import admin
import sys
#sys.path.append('..')
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_id>[0-9]+)/$', views.userview, name='userview'),
    url(r'^(?P<user_id>[0-9]+)/(?P<plan_id>[0-9]+)/$', views.planview, name='planview'),
    url(r'^upload/$', views.uploadview, name='uploadview')
]