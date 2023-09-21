from django.shortcuts import render, redirect
from .models import Maladie,Villes
import openai


# openai.api_key = ""

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



### Systeme de recommandation


def recommend_doctors(request):
    if request.method == 'POST':
        city = request.POST.get('ville')
        specialty = request.POST.get('symptoms')

        # Appel à OpenAI pour générer la recommandation des médecins
        openai.api_key = ''
        prompt = f"Trouvez des médecins à {city} spécialisés en {specialty}."
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            temperature=0.7,
            # n=5,
            stop=None,
            max_tokens=500,
        )

        doctors = response.choices[0].text.split("\n") 

        return render(request, 'pages/recommend_doctors.html', {'doctors': doctors})

    return render(request, 'pages/recommend_doctors.html')


def produit(request):
    return render(request,"pages/produit.html")


def specialites(request):
    return render(request, 'pages/specialites.html')
