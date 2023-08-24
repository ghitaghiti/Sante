from django.shortcuts import render
from .forms import wakha

def lkhra(request):
    if request.method=='POST' :
        data= wakha(request.POST)
        if data.is_valid:
            data.save()
    # dataobjs= Vnoms.objects.all()
    # return render(request, "pages/vnom.html", { 'serch': dataobjs })
    # return render(request, "pages/vnom.html", {'serch': Vnoms.objects.all()})
    return render(request, "pages/vnom.html", {'inp': lkhraForm })
