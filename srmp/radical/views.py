from django.shortcuts import render
from .models import Maladie,Villes
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
    if request.method == 'POST':
        patient_input = request.POST['symptoms']  # Assuming input field name is 'symptoms'
        doctor_recommendation = generate_doctor_recommendation(patient_input)
        return render(request, 'pages/recommandation.html', {'recommendation': doctor_recommendation})
    return render(request, 'pages/recommandation.html')

# pour generer un docteur a partir d'une liste des docteurs utilisant api d'openai
def generate_doctor_recommendation(patient_input):
    prompt = f"Patient symptoms: {patient_input}\nRecommended doctors:"
    openai.api_key = "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"
    response = open.Completion.create(
        engine="text-davinci-003",  # Choose an appropriate OpenAI engine
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()
