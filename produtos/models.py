from django.db import models

# Create your models here.

class Produto(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    nome_produto = models.CharField(max_length=30)
    descricao = models.TextField()
    valor = models.FloatField()
    foto = models.ImageField()
