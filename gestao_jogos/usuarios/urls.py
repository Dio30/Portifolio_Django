from django.urls import path
from .views import register_request, login_request, logout_request

urlpatterns = [
    path('registrar/', register_request, name='cadastro'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
]