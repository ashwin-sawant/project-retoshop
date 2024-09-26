# from django.urls import path
# from .import views

# urlpatterns = [
#     path('consumer/userdashboard/', views.userdashboard, name='userdashboard'),
#     path('consumer/userorder/', views.userorder, name='userorder')
# ]

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('orders/', views.userorder, name='userorder'),
]
