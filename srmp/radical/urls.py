from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home" ),
    path("inner/", views.innerpage),
    path("service/", views.service,name="services"),
    path("about/", views.propos,name="propos"),
    path("contact/", views.contact,name="contact"),
    path("login/", views.login,name="login"),
    path("signup/", views.signup,name="signup"),


]
