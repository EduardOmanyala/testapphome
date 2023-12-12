from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def home2(request):
    return render(request, 'core/home2.html')


def about(request):
    return render(request, 'core/about.html')


def selector(request):
    return render(request, 'core/select.html')

def contactus(request):
    return render(request, 'core/contactus.html')