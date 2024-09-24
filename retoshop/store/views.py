from django.shortcuts import render

def store(request):
    return render(request, "store.html")

def products(request):
    return render(request, "products.html")

def product(request):
    return render(request, "particular_product.html")

def cart(request):
    return render(request, "cart.html")
