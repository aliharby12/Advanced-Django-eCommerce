from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='list-api'),
    path('<int:id>', ProductDetailAPIView.as_view(), name='detail-api'),
    path('<int:id>/update', ProductUpdateAPIView.as_view(), name='update-api'),
    path('<int:id>/delete', ProductDeleteAPIView.as_view(), name='delete-api'),
    path('create', ProductCreateAPIView.as_view(), name='create-api'),
]
