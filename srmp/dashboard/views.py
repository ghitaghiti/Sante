from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout

def dashboardindex(request):
    context= {}
    return render(request, 'dashboard/dashboard/dashboard.html', context)

def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('medecins/docteurs.html')
		else:
			messages.success(request, "Error Logging In. Please Try Again...")
			return redirect('dashboard\dashboard\sign-in.html')
	else:
		return render(request, 'dashboard\dashboard\sign-in.html', {})



def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Registered...Congrats!!")
			return redirect('pages\home.html')

	else:
		form = SignUpForm()

	return render(request, 'dashboard\dashboard\sign-up.html', {"form": form})
