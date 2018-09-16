# coding: utf-8

import random
from datetime import datetime
import time
import io
import csv

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from item.api import views
from item.models import TaggedItem

import utils

class TestImport(TestCase):

    def setUp(self):
        pass


    _TEST_ROW_COUNT = 256

    def test_rm_orphans(self):
        # --- given 
        # client = Client()
        # data = utils._create_data(TestImport._TEST_ROW_COUNT)
        # csv_data = utils._create_csv(data)

        # --- when
        # response = client.post('/api/items/upload/', data={"file":csv_data} )
        # self.assertEqual(200, response.status_code)

        # --- then
        # items = TaggedItem.objects.all()
        # ...
        
        pass

    def test_rm_tags(self):
        pass
    
    def test_mv_tags(self):
        pass



    pass
