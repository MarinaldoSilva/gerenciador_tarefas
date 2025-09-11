from django.db import models
from django.conf import settings


class Tarefa(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    concluido = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    dono = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo}: {self.descricao}"
