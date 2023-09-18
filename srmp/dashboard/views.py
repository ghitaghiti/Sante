from django.shortcuts import render


def dashboardindex(request):
    context= {}
    return render(request, 'dashboard/dashboard/dashboard.html', context)


def signin(request):
    context= {}
    return render(request, 'dashboard/dashboard/sign-in.html', context)

def signup(request):
    context= {}
    return render(request, 'dashboard/dashboard/sign-up.html', context)
