from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
from .utils import get_address_info
import requests



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nome do Usuário'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha não pode ser semelhante informações pessoais.</li><li>Sua senha deve conter pelo menos 8 caracteres.</li><li>Sua senha não pode ser igual a anterior.</li><li>Sua senha deve conter letras e numeros.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirma senha'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"></span>'

class AddRecordForm(forms.ModelForm):
	nome = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"nome","class":"form-control"}),label="Nome")
	sobrenome = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"sobrenome","class":"form-control"}),label="Sobrenome")
	cep = forms.CharField(required=True,widget=forms.widgets.TextInput(attrs={"placeholder": "CEP", "class": "form-control"}),label="Cep")
	logradouro = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"endereco","class":"form-control"}),label="Logradouro")
	cidade = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"cidade","class":"form-control"}),label="Cidade")
	estado = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"estado","class":"form-control"}),label="Estado")
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"email","class":"form-control"}),label="Email")
	telefone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"telefone","class":"form-control"}),label="Telefone")

	def clean_cep(self):
		cep = self.cleaned_data.get('cep')
		address_info = get_address_info(cep)
		if not address_info:
			raise forms.ValidationError('CEP inválido')
		return cep

	class Meta:
		model = Record
		exclude = ("user",)

