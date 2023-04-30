from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.messages import constants


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = auth.authenticate(email = email, senha = senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha invalidos')
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
            messages.add_message(request, constants.ERROR, 'As senhas não iguais')
            return redirect(reverse('cadastro'))


        user = User.objects.filter(email = email)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'O email ja existe!')
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
        messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso!')
        return redirect(reverse('login')) 


def contato(request):
    return render(request, 'contato.html')