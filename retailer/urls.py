from django.urls import path
from .import views

urlpatterns = [
    path('retailer/retaildashboard/', views.retaildashboard, name='retaildashboard'),
    path('retailer/retailproducts/', views.retailproducts, name='retailproducts'),
    path('retailer/retailorders/', views.retailorders, name='retailorders')
]
