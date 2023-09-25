from django.shortcuts import render, redirect
from .models import Docteurs, DocteurSignUp
from .forms import AddDoctorForm

def docteurs(request):
    if 'searched' in request.GET:
        searched = request.GET['searched']
        data = Docteurs.objects.filter(fullname__icontains=searched)
    else:
        data = Docteurs.objects.all()
    doc={
      'medecin': data,
    }
    return render(request, 'medecins/docteurs.html',doc)



def adddoct(request):
    if request.method == 'POST':
        data= AddDoctorForm(request.POST, request.FILES)
        if data.is_valid:
            data.save()
    return render(request, 'medecins/zoldik.html', {'form': AddDoctorForm})


