from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from gpt.services.name_serializer import name_serializer

class TestViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        if pk is None or pk == "":
            return Response(status=400)

        title = name_serializer(pk)

        return Response(title)