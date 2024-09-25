from django.urls import path
from .import views

urlpatterns = [
    path('consumer/userdashboard/', views.userdashboard, name='userdashboard'),
    path('consumer/userorder/', views.userorder, name='userorder')
]