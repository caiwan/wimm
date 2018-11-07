# coding: utf-8
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from django.core.files.base import ContentFile

from smartimport.models import RawItem

class TestSmartImportOTP(TestCase):

    def test_import_csv(self):
        client = Client()
        
        # given 
        with open('./smartimport/tests/data/raw.csv') as infile:
            headers = {'content-type': 'multipart/form-data'}
            csv_file = ContentFile(infile.read()) # Propbaly there's a more elegant method
            csv_file.name = "Untitled.csv"

            response = client.post('/api/smartimport/upload/', data={"file":csv_file, 'type':4}, headers=headers)
            self.assertEqual(200, response.status_code)

            responseBody = response.json()
            if 'error' in responseBody:
                self.fail(msg=responseBody['error'])

            self.assertTrue('items' in responseBody)

            pass

        # when 
        response = client.get('/api/smartimport/items/', headers={'content-type': 'application/json'})
        responseBody = response.json()

        print(responseBody)

        # then
        for item in responseBody['items']:
            # print(item)
            self.assertTrue('id' in item)
            self.assertTrue('date' in item)
            self.assertTrue('price' in item)
            self.assertTrue('text' in item)
            self.assertTrue('tags' in item)
            db_item = RawItem.objects.get(id=item['id'])
            # print(db_item)
            self.assertEquals(item['id'], db_item.id)
            self.assertEquals(item['text'], db_item.content)
            pass

        pass

    pass
