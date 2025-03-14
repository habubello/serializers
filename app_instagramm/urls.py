from django.urls import path
from app_instagramm.views import (
    ProductListCreateView, ProductDetailView,
    CategoryListCreateView, CategoryDetailView
)

urlpatterns = [
    # Products urls
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),


    # categori urls
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]
