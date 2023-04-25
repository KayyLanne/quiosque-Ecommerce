from django.contrib import admin
from django.urls import path
from produtos.views import home, login, cadastro, produto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login),
    path('cadastro/', cadastro),
    path('produto/', produto),
]
