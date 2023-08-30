from django.shortcuts import render
from .models import Patient

def patient(requet):
    return render(requet,'patients/patient.html', {'property': Patient.objects.all() })

