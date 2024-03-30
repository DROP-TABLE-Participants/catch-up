from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from gpt.services.name_serializer import name_serializer

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticated]

    """
    A simple ViewSet for listing or retrieving products.
    """
    def list(self, request):
        # get all products
        return Response(ProductSerializer(Product.objects.all(), many=True).data)
        #return Response("""name_serializer("Смартфон Samsung Galaxy A34, 6GB, 128GB, Awesome Graphite - SM-A346BZKAEUE")""")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # route to delete all
    @action(methods=["DELETE"], detail=False)
    def delete(self, request):
        delete_albums = self.queryset.all()

        delete_albums.delete()
        return Response(self.serializer_class(delete_albums, many=True).data)

