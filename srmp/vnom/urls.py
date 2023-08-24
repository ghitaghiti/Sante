from django.urls import path
from . import views

urlpatterns = [
    path('vnom/', views.vanoma, name= 'vnom'),
]
