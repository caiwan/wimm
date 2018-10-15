# coding: utf-8

import io

from django.db import transaction

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from smartimport.processors import dispatch as DispatchProcess
from smartimport.models import RawItem

class Import(ModelViewSet):
    pass

class Upload(APIView):
    def post(self, request, format=None):
        text = request.data['file'].read().decode(encoding='UTF-8',errors='strict')
        type = request.data['type']

        try:
            parser = DispatchProcess(type)
            if not parser:
                raise RuntimeError("Invlaid parser or not found")

            result = parser.preprocess(io.StringIO(text))

            with transaction.atomic():
                for item in result:
                    model = RawItem.objects.create(
                        type=int(type),
                        content=item['text']
                    )
                    # item.update(('id', model.id))
                    item['id'] = model.id
                pass

            return Response({'items': result})
        except Exception as e:
            return Response({'error': str(e)})

    pass
