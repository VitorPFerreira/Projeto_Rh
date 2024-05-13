from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record
import requests

def home(request):
	filtro_nome = request.GET.get('filtro_nome')

	# Se houver um parâmetro de filtro de nome na URL
	if filtro_nome:
		# Ajuste a consulta para filtrar os funcionários pelo nome
		records = Record.objects.filter(nome__icontains=filtro_nome)
		return render(request, 'usuario/home.html', {'records': records})
#Verificar Loggin
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		#Autenticar login
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request,"Voce esta logado!")
			return redirect('home')
		else:
			messages.success(request,"Usuario ou Senha incorreto, Tente Novamente!")
			return redirect('home')
	else:
		records = Record.objects.all()
		return render(request,'usuario/home.html',{'records':records})

#def login_user(request):
    #pass
def logout_user(request):
    logout(request)
    messages.success(request, "Usuario Desconectado")
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Registrado com sucesso! Bem-vindo!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'usuario/register.html', {'form':form})

	return render(request, 'usuario/register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'usuario/record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "Você deve estar logado para visualizar essa página!")
        return redirect('home')

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Deletado com Sucesso")
		return redirect('home')
	else:
		messages.success(request, "Você deve estar logado para visualizar essa página!")
		return redirect('home')
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Cadastrado com Sucesso!")
				return redirect('home')
		return render(request, 'usuario/add_record.html', {'form':form})
	else:
		messages.success(request, "Você deve estar logado para visualizar essa página!")
		return redirect('home')
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request,"Registro atualizado")
			return redirect('home')
		return render(request, 'usuario/update_record.html', {'form': form})
	else:
		messages.success(request, "Você deve estar logado para visualizar essa página!")
		return redirect('home')

