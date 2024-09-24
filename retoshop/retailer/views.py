from django.shortcuts import render


def retaildashboard(request):
    return render(request, 'retaildashboard.html')


def retailorders(request):
    return render(request, "retailorders.html")

def retailproducts(request):
    return render(request, "retailproducts.html")