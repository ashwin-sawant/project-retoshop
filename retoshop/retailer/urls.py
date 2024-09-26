from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('retailer/dashboard/', views.retailer_dashboard, name='retailer_dashboard'),
    path('retailer/add-products/', views.add_products, name='add_products'),
    path('retailer/orders/', views.retailer_orders, name='retailer_orders'),
]
