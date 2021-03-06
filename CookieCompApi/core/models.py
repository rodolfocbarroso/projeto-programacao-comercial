from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoriaPai = models.ForeignKey('self', unique=False, null=True, blank=True, on_delete=models.SET_NULL, related_name="filhoCategoria")
    ativa = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagemUrl = models.CharField(max_length=1000)
    conteudo = models.BinaryField()
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
