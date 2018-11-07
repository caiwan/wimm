# coding: utf-8

from rest_framework.serializers import ModelSerializer

from item.api.serializers import ItemSerializer

from smartimport.models import RawItem

class RawItemSerializer(ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = RawItem
        fields = ('id', 'date', 'price', 'tags')
