from django.contrib import admin
from django.urls import path, include
from produtos.views import home, produto
from usuarios.views import login, cadastro, contato
from carrinho.views import carrinho

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('produto/', produto, name='produto'),
    path('usuarios/', include('usuarios.urls')),
    path('carrinho/', carrinho, name='carrinho'),
    ]
