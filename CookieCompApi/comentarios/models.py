from django.contrib.auth.models import User
from django.db import models
from core.models import Artigo


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    camentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.usuario.username
