# coding: utf-8

from django.conf.urls import url

from wimm.api import api

from smartimport.api.views import Imports, Upload

# api.register(r'import', Imports, 'import')

urlpatterns = [
    url(r'^smartimport/upload/$', Upload.as_view())
]
