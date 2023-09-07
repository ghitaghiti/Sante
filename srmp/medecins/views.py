from django.shortcuts import render, redirect
from .models import Docteurs, DocteurSignUp
from .forms import AddDoctorForm

def docteurs(request):
    doc={
      'medecin': Docteurs.objects.all(),
    }
    return render(request, 'medecins/docteurs.html',doc)

# def apoint(request):
     
#     return render(request, 'medecins/apoint.html')

def signup(request):
    if request.method == 'POST':
        # Process the valid form data
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = DocteurSignUp(fullname=fullname, email=email, password1=password1, password2=password2)
        user.save()

        return redirect('home')
    return render(request, "pages/signup.html")

def adddoct(request):
    if request.method == 'POST':
        data= AddDoctorForm(request.POST, request.FILES)
        if data.is_valid:
            data.save()
    return render(request, 'medecins/zoldik.html', {'form': AddDoctorForm})


