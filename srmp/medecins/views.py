from django.shortcuts import render
from .models import Docteurs

def docteurs(request):
    
    return render(request, 'medecins/docteurs.html')

#  def apoint(request):
     
#      return render(request, 'medecins/apoint.html')