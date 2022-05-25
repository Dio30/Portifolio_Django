from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .forms import NewUserForm

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Usuario cadastrado com sucesso" )
			return redirect("login.html")
		messages.error(request, "Cadastro preenchido incorretamente, Tente novamente. ")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request,f"Voce está logado como {username}.")
				return redirect("/")
			else:
				messages.warning(request,f"Voce deslogou como {username}.")
		else:
			messages.error(request,"Usuario ou senha incorretos, tente novamente.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})
