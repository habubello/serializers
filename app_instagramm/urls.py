from django.urls import path
from app_instagramm.views import (
    ProductListCreateView, ProductDetailView,
    CategoryListCreateView, CategoryDetailView, CommentListView, ProductCommentListView
)

urlpatterns = [
    # Products urls
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),


    # category urls
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    #comment urls

    path('comments/',CommentListView.as_view(),name='comment_list'),
    path('products/comments/<int:product_id>', ProductCommentListView.as_view(), name='product-comments'),

]
