__author__ = 'satish'
from django.conf.urls import url, patterns

from bought.views import index

urlpatterns = patterns('',
                      url(r'^$', index, name = 'index'),
                      )