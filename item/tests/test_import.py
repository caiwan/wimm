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
from django.core.files.base import ContentFile

from item.api import views
from item.models import TaggedItem

# from utils import *
from . import utils

class TestImport(TestCase):

    _TEST_ROW_COUNT = 256

    def test_import_csv(self):
        # given 
        client = Client()
        headers = {'content-type': 'multipart/form-data'}
        data = utils.create_data(TestImport._TEST_ROW_COUNT)
        csv_data = utils.create_csv(data)
        csv_file = ContentFile(csv_data)
        csv_file.name = "Untitled.csv"

        # when
        response = client.post('/api/items/upload/', data={"file":csv_file}, headers=headers)
        self.assertEqual(200, response.status_code)

        responseBody = response.json()
        if 'error' in responseBody:
            self.fail(msg=responseBody['error'])

        self.assertTrue('imported' in responseBody)

        # then
        items = TaggedItem.objects.all()
        self.assertEquals(len(data), items.count()) 
        
        # for i in range(len(data)):
        #   pass

        pass

    pass
