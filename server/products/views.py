from rest_framework import permissions
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

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
    def list(self, request, *args, **kwargs):
        # get all products
        user_id = self.request.user.id
        return Response(ProductSerializer(Product.objects.filter(owner=user_id), many=True).data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        user_id = self.request.user.id
        if serializer.instance.owner.id != user_id:
            return Response({"error": "You are not the owner of this product"}, status=403)
        serializer.save(owner=self.request.user)
        return Response(serializer.data)

    def perform_destroy(self, instance):
        user_id = self.request.user.id
        if instance.owner.id != user_id:
            return Response({"error": "You are not the owner of this product"}, status=403)
        instance.delete()
        return Response(status=204)

    def retrieve(self, request, *args, **kwargs):
        user_id = self.request.user.id
        instance = self.get_object()
        if instance.owner.id != user_id:
            return Response({"error": "You are not the owner of this product"}, status=403)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

