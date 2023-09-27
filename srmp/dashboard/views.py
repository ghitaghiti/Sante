from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def dashboardindex(request):
    context= {}
    return render(request, 'dashboard/dashboard/dashboard.html', context)

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('dashboard')
		else:
			messages.success(request, "Error Logging In. Please Try Again...")
			return redirect('login')
	else:
		return render(request, 'dashboard/dashboard/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


def register_user(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Registered.")
			return redirect('dashboard')

	else:
		form = SignUpForm()

	return render(request, 'dashboard/dashboard/register.html', {"form": form})

def buttons(request):
	context= {}
	return render(request, 'dashboard/components/buttons.html', context)

def forms(request):
	context= {}
	return render(request, 'dashboard/components/foms.html', context)

def modals(request):
	context= {}
	return render(request, 'dashboard/components/modals.html', context)

def notifications(request):
	context= {}
	return render(request, 'dashboard/components/notifications.html', context)

def typography(request):
	context= {}
	return render(request, 'dashboard/components/typography.html', context)

def erorrfour(request):
	context= {}
	return render(request, 'dashboard/dashboard/404.html', context)

def erorrfive(request):
	context= {}
	return render(request, 'dashboard/dashboard/500.html', context)

def bootstraptable(request):
	context= {}
	return render(request, 'dashboard/tables/bootstrap-tables.html', context)

def settings(request):
	context= {}
	return render(request, 'dashboard/settings.html', context)

def transactions(request):
	context= {}
	return render(request, 'dashboard/transactions.html', context)

def forgotpassword(request):
	context= {}
	return render(request, 'dashboard/dashboard/forgotpassword.html', context)

def resetpassword(request):
	context= {}
	return render(request, 'dashboard/dashboard/reset-password.html', context)

def lock(request):
	context= {}
	return render(request, 'dashboard/dashboard/lock.html', context)

