from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import auth


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(email = email, senha = senha)

        if not user:
            return redirect(reverse('login'))

        auth.login(request, user)
        return redirect('produtos')    

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        telefone = request.POST.get('telefone')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        numero = request.POST.get('numero')

        if not senha == confirmar_senha:
            return redirect(reverse('cadastro'))


        user = User.objects.filter(email = email)

        if user.exists():
            return redirect(reverse('cadastro'))

        user = User.objects.create_user(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            senha = senha,
            telefone = telefone,
            cidade = cidade,
            estado = estado,
            numero = numero,
        ) 

        return redirect(reverse('login')) 

def confirmacaoCadastro(request):
    return render(request, 'confirmacaoCadastro.html')

def contato(request):
    return render(request, 'contato.html')