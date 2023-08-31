from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("radical.urls")),
    path("medecins/", include("medecins.urls")),
    path("patient/", include("patient.urls")),
   
   

]
