__author__ = 'satish'
from django.conf.urls import url, patterns

from bought import views

urlpatterns = patterns('',
                      url(r'^$', views.index, name = 'index'),
                      url(r'^(?P<id>\d+)/$', views.detail, name = 'detail')
                      )