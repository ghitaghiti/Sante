from django.shortcuts import render
from .models import Docteurs

def docteurs(request):
    doc={
      'medecin': Docteurs.objects.all(),
    }
    return render(request, 'medecins/docteurs.html',doc)

# def apoint(request):
     
#     return render(request, 'medecins/apoint.html')

