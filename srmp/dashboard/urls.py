from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboardindex, name='dashboard'),    
    path('signin/', views.signin, name='signin'),    
    path('signup/', views.signup, name='signup'),    
    # path('derror404/', views.dashboardindex, name='error404'),    
   
]
