from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboardindex, name='dashboard'),    
    path('login/', views.login_user, name='login'),
	path('logout/', views.logout_user, name='logout'),
	path('register/', views.register_user, name='register'),
	path('buttons/', views.buttons, name='buttons'),
	path('forms/', views.forms, name='forms'),
	path('modals/', views.modals, name='modals'),
	path('notifications/', views.notifications, name='notifications'),
	path('typography/', views.typography, name='typography'),
	path('404/', views.erorrfour, name='404'),
	path('bootstraptable/', views.bootstraptable, name='bootstrap-table'),
	path('settings/', views.settings, name='settings'),
	path('transactions/', views.transactions, name='transactions'),
	path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
	path('reset-password/', views.resetpassword, name='reset-password'),
	path('lock/', views.lock, name='lock'),
	path('500/', views.erorrfive, name='500'),
]
