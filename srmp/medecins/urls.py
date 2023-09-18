from django.urls import path
from . import views


urlpatterns = [
    
   path("",views.docteurs,name='medecin'),
   path("signin/",views.signin,name='signin'),
   path("adddocteur/",views.adddoct,name='adddoct'),
   
]
