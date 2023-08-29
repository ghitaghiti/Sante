from django.urls import path
from . import views


urlpatterns = [
   path("",views.docteurs,name='medecin'),
   path("apoint/",views.apoint,name='rendez-vous'),
   
]