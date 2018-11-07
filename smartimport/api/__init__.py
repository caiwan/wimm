# coding: utf-8

from django.conf.urls import url

from wimm.api import api

from smartimport.api.views import ItemPopulate, Upload

api.register(r'items', ItemPopulate, 'items')

urlpatterns = [
    url(r'^upload/$', Upload.as_view())
]
