from django.contrib import admin
from django.urls import path
from produtos.views import home, produto
from usuarios.views import login, cadastro, contato
from carrinho.views import carrinho

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home_quiosque'),
    path('login/', login, name='login_cliente'),
    path('cadastro/', cadastro, name='cadastro_cliente'),
    path('produto/', produto, name='detalhe_produto'),
    path('contato/', contato, name='contato_quiosque'),
    path('carrinho/', carrinho, name='carrinho_quiosque'),
    path('confirmacaoCadastro/', carrinho, name='confirmacao_cadastro'),
    ]
