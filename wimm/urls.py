# coding: utf-8

from django.conf.urls import url

from item.views import ItemApi, ItemList, ItemTagsAuto, Index

urlpatterns = [
    url(r'^$', ItemList.as_view(), name='index'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/items/', ItemApi.as_view(), name='item-api'),
    url(r'^autocomplete/tags/$', ItemTagsAuto.as_view(), name='item-tags-auto'),

    url(r'^vue/', Index.as_view(), name='vue')
]
