from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    email = models.EmailField('E-mail',unique=True)
    senha = models.CharField(max_length=10)
    telefone = models.CharField(max_length=10)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    numero = models.IntegerField(null=True)


    def __str__(self):
        return self.nome + ' ' + self.sobrenome

