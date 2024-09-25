from django.urls import path
from .import views

urlpatterns = [
    path('store/', views.store, name='store'),
    path('store/cart', views.cart, name='cart'),
    path('store/products', views.products, name='products'),
    path('store/product', views.product, name='product'),
]