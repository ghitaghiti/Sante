from django.shortcuts import render
from .models import Maladie,Villes
from django.http import HttpResponse
import openai
from medecins.models import Docteurs
from patient.models import Patient


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

def login(request):
    return render(request,"pages/login.html")

def signup(request):
    return render(request,"pages/signup.html")

### Systeme de recommandation

def recommend_doctors(request):
    if request.method == "POST":
        patient_input = request.POST.get('symptoms') # Assuming input field name is 'symptoms'
        patient_location = request.POST.get('ville')
        doctor_recommendation = generate_doctor_recommendation(patient_input, patient_location)
        return render(request, 'pages/recommandation.html', {'recommendation': doctor_recommendation})

    return render(request, 'pages/recommandation.html')

# pour generer un docteur a partir d'une liste des docteurs utilisant api d'openai
openai.api_key = ""
def generate_doctor_recommendation(patient_input, patient_location):
    prompt = f"Je recherche des médecins au Maroc spécialisés en ces symptômes {patient_input} et situés à {patient_location}. Pouvez-vous recommander des médecins avec leurs informations ?"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
        stop=None,
        temperature=0.7
    )

    recommendations_text = response.choices[0].text.strip()
    recommendations = recommendations_text.split('\n') 
    recommendations = [line.strip() for line in recommendations if line.strip()]
    return recommendations

def produit(request):
    return render(request,"pages/produit.html")

def comments(request):
    return render(request,"pages/comments.html")