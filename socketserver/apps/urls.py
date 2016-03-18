__author__ = 'Prakasa'

from django.conf.urls import include, url
from . import views

urlpatterns = {
    url(r'^$', views.index, name='index'),
    url(r'^foobar/(?P<id>[0-9]+)/$', views.foobar, name='foobar')
}
