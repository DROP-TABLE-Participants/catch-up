from rest_framework import serializers

from .models import Product

from gpt.services.name_serializer import name_serializer

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    image_url = serializers.ImageField(required=False)
    owner = serializers.ReadOnlyField(source='owner.id')
    serialized_name = serializers.CharField(source=name_serializer("name"))

    class Meta:
        model = Product
        fields = ('__all__')