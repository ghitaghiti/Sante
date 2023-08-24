from django.shortcuts import render
from .models import Docteurs

def doct(request):
    
    return render(request, 'medecins/doct.html', {})

# def apoint(request):
#     pass
    # return render(request, 'medecins/apoint.html', {'property': Docteur.objects.all() })