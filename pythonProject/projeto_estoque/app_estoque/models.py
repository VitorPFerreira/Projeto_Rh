from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)


def __str__(self):
    return(
        f"{self.nome} {self.sobrenome}"
    )