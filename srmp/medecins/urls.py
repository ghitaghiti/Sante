from django.urls import path
from . import views


urlpatterns = [
    
   path("",views.docteurs,name='medecin'),
   
   path("signup/",views.signup,name='signup'),
   path("adddocteur/",views.adddoct,name='adddoct'),
   
]
