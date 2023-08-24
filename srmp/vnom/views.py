from django.shortcuts import render
from .forms import VnomForm

def vanoma(request):
    if request.method=='POST' :
        data= VnomForm(request.POST)
        if data.is_valid:
            data.save()
    # dataobjs= Vnoms.objects.all()
    # return render(request, "pages/vnom.html", { 'serch': dataobjs })
    # return render(request, "pages/vnom.html", {'serch': Vnoms.objects.all()})
    return render(request, "pages/vnom.html", {'inp': VnomForm })
