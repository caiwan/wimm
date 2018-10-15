# coding: utf-8

from django.conf.urls import url

from wimm.api import api

from smartimport.api.views import Import, Upload

# api.register(r'import', Imports, 'import')

urlpatterns = [
    url(r'^upload/$', Upload.as_view())
]
