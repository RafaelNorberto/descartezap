from django.db import models
from django.contrib.auth.models import User

class CadastroDoadores(models.Model):
    nome = models.CharField(max_length=20, null=False, blank=False)
    sobrenome = models.CharField(max_length=20, null=False, blank=False)
    dataNascimento = models.CharField(max_length=20, null=False, blank=False)
    endereco = models.CharField(max_length=20, null=False, blank=False)
    numero = models.CharField(max_length=20, null=False, blank=False)
    bairro = models.CharField(max_length=20, null=False, blank=False)
    cidade = models.CharField(max_length=20, null=False, blank=False)
    telefonefixo = models.CharField(max_length=20, null=False, blank=False)
    celular = models.CharField(max_length=20, null=False, blank=False)
    Intencao = models.CharField(max_length=20, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Publico:
        db_table = 'cadastrodoadores'

