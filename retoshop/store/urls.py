from django.urls import path
from .import views
from django.urls import path
from .views import store, add_to_cart, view_cart, remove_from_cart, products_view

urlpatterns = [
    path('store/', views.store, name='store'),
    path('store/cart', views.view_cart, name='view_cart'),
    path('store/<int:category_id>/', views.products, name='products'),
    path('store/product', views.product, name='product'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('category/<int:category_id>/', products_view, name='products_by_category'),  # Products by category
    
]




