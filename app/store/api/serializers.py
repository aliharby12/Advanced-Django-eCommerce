from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from store.models import Product

class ProductSerializer(ModelSerializer):
    """create a serializers to list all products"""
    url = HyperlinkedIdentityField(view_name='detail-api', lookup_field='id')
    class Meta:
        model = Product
        fields = ['url', 'id', 'user', 'name', 'price', 'digital']
