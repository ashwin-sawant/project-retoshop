from django.urls import path
from .import views

urlpatterns = [
    path('authentication/login/', views.login, name='login'),
    path('authentication/register/', views.register, name='register'),
    path('authentication/verify/', views.verify, name='verify'),
]