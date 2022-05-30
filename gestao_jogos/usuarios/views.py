from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .forms import UsuariosForm
from django.contrib.auth.models import Group

def register_request(request):
    if request.method == "POST":
        form = UsuariosForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Clientes')
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            messages.success(request, f"Usuario cadastrado com sucesso por {username}")
            return redirect("login")
        messages.error(request, "Algum dado foi preenchido incorretamente, tente novamente.")     
    form = UsuariosForm()
    return render (request, template_name="register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Voce está logado como {username}.")
                return redirect("/")
            else:
                return redirect("login")
        else:
            messages.error(request,"Usuario ou senha incorretos, tente novamente.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.success(request, "Voce deslogou com sucesso.")
    return redirect ('login')