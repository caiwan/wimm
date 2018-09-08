# coding: utf-8

import random
from datetime import datetime
import time
import io
import csv

from item.api import views
from item.models import TaggedItem

from django.conf import settings
# from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

class TestImport(TestCase):

    _TEST_ROW_COUNT = 256

    def test_import_csv(self):
        # given 
        client = Client()
        data = TestImport._create_data(TestImport._TEST_ROW_COUNT)
        csv_data = TestImport._create_csv(data)

        # when
        response = client.post('/api/items/upload/', data={"file":csv_data} )
        self.assertEqual(200, response.status_code)

        # then
        items = TaggedItem.objects.all()
        # ...
        
        pass

    @staticmethod
    def _create_data(count):
        # I have to admit that I'm a terrible person when I commit to add 
        # characters other than ASCII into the code, please don't hurt me
        tags = ['cica', 'kutya', 'malac', 'árvíztűrőtükörfúrógép']
        data = []
        for i in range (count):
            random_ts = time.time() - random.randint(-30, 30) * 60 * 60 * 24 
            random_date = datetime.fromtimestamp(random_ts).strftime('%Y-%m-%d')
            random_tags = random.choice(tags)
            data.append(
                {"date":random_date, 
                "price":random.randint(-100, 100), 
                "tags":random_tags}
            )
        return data

    @staticmethod
    def _create_csv(data):
        csv_data = None

        mem_io = io.BytesIO()
        # with mem_io as f:  # Just use 'w' mode in 3.x
        f = mem_io

        if data:
            w = csv.DictWriter(f, data[0].keys())
            w.writeheader()

            for row in data:
                w.writerow(row)

        csv_data = mem_io.getvalue()

        return csv_data

    pass
