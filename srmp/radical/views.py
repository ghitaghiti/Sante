from django.shortcuts import render
from .models import Maladie,Villes

def home(request):
    maladieville ={
        'maladie': Maladie.objects.all(),
        'ville': Villes.objects.all(),
    }
    return render(request,"pages\home.html", maladieville)


def innerpage(request):
    return render(request,"pages\inner-page.html")

def service(request):
    return render(request,"pages\services.html")

def propos(request):
    return render(request,"pages/about.html")

def contact(request):
    return render(request,"pages/contact.html")
