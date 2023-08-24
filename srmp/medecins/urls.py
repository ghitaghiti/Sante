from django.urls import path
from . import views


urlpatterns = [
   path("",views.doct,name='docteur'),
   # path("apoint/",views.apoint,name='docteur'),
    
]