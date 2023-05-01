from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def produto(request):
    return render(request, 'produto.html')

