from django.urls import path
from app_instagramm.views import ProductAPIView

urlpatterns = [
    path('api/products/', ProductAPIView.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),
]
