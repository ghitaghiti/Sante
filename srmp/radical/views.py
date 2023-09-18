from django.shortcuts import render, redirect
from .models import Maladie,Villes,Question
import openai
from medecins.models import Docteurs
from patient.models import Patient
from .models import Question

# openai.api_key = "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"

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
        city = request.POST.get('ville')
        specialty = request.POST.get('symptoms')

        # Appel à OpenAI pour générer la recommandation des médecins
        openai.api_key = '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'
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


# def recommend_doctors(request):
#     if request.method == "POST":
#         print('in if')
#         patient_input = request.POST('symptoms')  # Assuming input field name is 'symptoms'
#         doctor_recommendation = generate_doctor_recommendation(patient_input)
#         return render(request, 'pages/recommandation.html', {'recommendation': doctor_recommendation})
#     print('out if')
#     return render(request, 'pages/recommandation.html')

# # pour generer un docteur a partir d'une liste des docteurs utilisant api d'openai
# def generate_doctor_recommendation(patient_input):
#     prompt = f"Patient symptoms: {patient_input}\nRecommended doctors:"
#     response = openai.Completion.create(
#         engine="text-davinci-003",  # Choose an appropriate OpenAI engine
#         prompt=prompt,
#         max_tokens=500,
#     )
#     return response.choices[0].text.strip()

def produit(request):
    return render(request,"pages/produit.html")


def faq(request):
    questions = Question.objects.all()
    # return render(request, "pages/faq.html", {'questions': questions})
    if request.method == 'POST':
        question_text = request.POST['quest']
        question = Question(question_text=question_text)
        question.save()
        return redirect('faq')
    return render(request, 'pages/faq.html')
