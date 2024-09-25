from django.shortcuts import render

def userdashboard(request):
    return render(request, "userdashboard.html")


def userorder(request):
    return render(request, "userorder.html")