from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ativa = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
