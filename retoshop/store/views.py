from django.shortcuts import render
from .models import Category

def store(request):
    categories = Category.objects.all()
    return render(request, "store.html",{'categories':categories})

def products(request):
    return render(request, "products.html")

def product(request):
    return render(request, "particular_product.html")

def cart(request):
    return render(request, "cart.html")
