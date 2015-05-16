__author__ = 'oleg'
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dis/$', views.disease, name='disease'),
    url(r'^dis/(?P<dis_id>[0-9]+)$', views.diseaseById, name='diseaseById'),
    url(r'^case$', views.case, name='case'),
    url(r'^case/(?P<case_id>[0-9]+)$', views.caseById, name='caseById'),
]