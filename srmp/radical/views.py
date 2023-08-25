from django.shortcuts import render

def home(request):
    return render(request,"pages\home.html")


def innerpage(request):
    return render(request,"pages\inner-page.html")
def service(request):
    return render(request,"pages\services.html")
def propos(request):
    return render(request,"pages/about.html")
    
