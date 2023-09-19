from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile


def dashboardindex(request):
    context= {}
    return render(request, 'dashboard/dashboard/dashboard.html', context)


def signin(request):
    context= {}
    return render(request, 'dashboard/dashboard/sign-in.html', context)

# def signup(request):
#     context= {}
#     return render(request, 'dashboard/dashboard/sign-up.html', context)





def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            # Créez un nouvel utilisateur avec l'email et le mot de passe fournis
            user = User.objects.create_user(username=email, email=email, password=password)
            
            # Créez un profil utilisateur associé
            user_profile = UserProfile(user=user)
            user_profile.save()
            
            # Redirigez l'utilisateur vers une page de confirmation ou une autre page appropriée
            return redirect('pages/home')
        else:
            # Les mots de passe ne correspondent pas, vous pouvez effectuer un traitement supplémentaire ici
            pass

    return render(request, 'dashboard/dashboard/sign-up.html')