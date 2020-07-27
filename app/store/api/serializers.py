from rest_framework.serializers import ModelSerializer
from store.models import Product

class ProductSerializer(ModelSerializer):
    """create a serializers to list all products"""
    class Meta:
        model = Product
        fields = ['id', 'user', 'name', 'price', 'digital']
