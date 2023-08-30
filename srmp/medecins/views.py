from django.shortcuts import render
from .models import Docteurs, Sicks

def docteurs(request):
    
    return render(request, 'medecins/docteurs.html')

def apoint(request):
     
    return render(request, 'medecins/apoint.html')

def sick(request):
    dataobject= Sicks.objects.all()
    return render(request,"medecins/apoint.html",{'maladie': dataobject})