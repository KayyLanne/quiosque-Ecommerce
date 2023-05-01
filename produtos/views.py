from django.shortcuts import render
from django.views.generic import ListView
from .models import Produto

def home(request):
    produtos = Produto.objects.all()
    context = {
        "produtos": produtos
    }
    return render(request, 'home.html', context)

def produto(request):
    return render(request, 'produto.html')

