from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404

class NewUserForm(UserCreationForm):
	grupo = forms.ModelChoiceField(queryset=Group.objects.filter(name__in=['Usuarios']), required=True)
	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user

	def form_valid(self, form):
		grupo = get_object_or_404(Group, name=form['Usuarios'].name)
		url = super().form_valid(form)
		self.object.add(grupo)
		self.object.save()
		return url