from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateAPIView,
                                     DestroyAPIView,
                                     CreateAPIView
                                     )
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from store.models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import (IsAdminUser,
                                        IsAuthenticatedOrReadOnly,
                                        IsAuthenticated
                                        )
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import ProductPageNumberPagination, ProductLimitOffsetPagination

@method_decorator(login_required, name='dispatch')
class ProductListAPIView(ListAPIView):
    """create a class to list all products"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__first_name', 'name', 'price']
    pagination_class = ProductLimitOffsetPagination

@method_decorator(login_required, name='dispatch')
class ProductDetailAPIView(RetrieveAPIView):
    """create a class to retrive details of a product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    # define the delete function
    def delete(self, request, id):
        queryset = get_object_or_404(Product, id)
        queryset.delete()

@method_decorator(login_required, name='dispatch')
class ProductUpdateAPIView(RetrieveUpdateAPIView):
    """create a class to update a product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,]
    lookup_field = 'id'

@method_decorator(login_required, name='dispatch')
class ProductDeleteAPIView(DestroyAPIView):
    """create a class to delete a product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

@method_decorator(login_required, name='dispatch')
class ProductCreateAPIView(CreateAPIView):
    """create a class to create a new product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,]

    # associate every product with it's user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
