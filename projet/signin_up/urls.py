'''urls de l'application signin_up'''

from django.urls import path
from . import views

urlpatterns = [
    path('signin_up/', views.HomePageView.as_view(), name='home'),
	path('', views.accueil, name='accueil'),
	path('signin_up/', views.SignUp.as_view(), name='signup'),
]