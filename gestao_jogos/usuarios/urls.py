from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.CadastrarUsuario.as_view(), name='cadastrar'),
]