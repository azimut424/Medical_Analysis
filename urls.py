
from django.urls import path

from . import views

urlpatterns = [

    path('acceuil/', views.acceuil, name='acceuil'),
    path('SingUp/', views.SingUp, name='SingUp'),
    path('SingIn/', views.SingIn, name='SingIn'),
    path('chat/', views.chat, name='chat'),
    path('chatlive/', views.chatlive, name='chatlive'),
    path('info_patient/', views.info_patient, name='info_patient'),
    path('logout_app/', views.liste_consultation, name = 'liste_consultation'),
    path('liste_consultation/', views.logout_app, name = 'logout_app'),
    path('adminAddMalaria/',views.adminAddMalaria, name='adminAddMalaria')
]