from django.db import models


class CadastroDoadores(models.Model):
    cpf = models.CharField(max_length=11, null=False, blank=False)
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
    quantidade = models.FloatField(verbose_name='Quantidade (l)')
    descricao = models.CharField(max_length=300, null=False, blank=False, verbose_name="Descrição")
    d_cpf = models.ForeignKey(CadastroDoadores, on_delete=models.CASCADE)


    def __str__(self):
        return "{} ({})".format(self.quantidade, self.d_cpf.bairro)
