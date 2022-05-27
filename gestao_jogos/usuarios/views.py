from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib import auth

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuario cadastrado com sucesso" )
            return redirect("login")
        messages.error(request, "Cadastro preenchido incorretamente ou esse usuario já existe, tente novamente. ")
    form = NewUserForm()
    return render (request, template_name="register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
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