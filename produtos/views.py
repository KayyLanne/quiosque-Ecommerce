from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def produto(request):
    return render(request, 'produto.html')

def contato(request):
    return render(request, 'contato.html')

def carrinho(request):
    return render(request, 'carrinho.html')