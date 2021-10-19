from django.db import models


class CadastroDoadores(models.Model):
    nome = models.CharField(max_length=20, null=False, blank=False)
    sobrenome = models.CharField(max_length=20, null=False, blank=False)
    dataNascimento = models.DateField(max_length=20, null=False, blank=False)
    endereco = models.CharField(max_length=20, null=False, blank=False)
    numero = models.CharField(max_length=20, null=False, blank=False)
    bairro = models.CharField(max_length=20, null=False, blank=False)
    cidade = models.CharField(max_length=20, null=False, blank=False)
    telefonefixo = models.CharField(max_length=20, null=False, blank=False)
    celular = models.CharField(max_length=20, null=False, blank=False)
    Intencao = models.CharField(max_length=20, null=False, blank=False)

    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.nome, self.bairro)


class QtDoacao(models.Model):
    d_celular = models.ForeignKey(CadastroDoadores, on_delete=models.CASCADE)
    quantidade = models.FloatField(verbose_name='Quantidade (l)')
    descricao = models.CharField(max_length=300, null=False, blank=False, verbose_name="Descrição")

    def __str__(self):
        return "{} ({})".format(self.d_celular, self.d_celular.quantidade)
