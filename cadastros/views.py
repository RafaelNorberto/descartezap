from django.views.generic.edit import CreateView
from .models import CadastroDoadores, QtDoacao
from django.urls import reverse_lazy


class CadastroDoadoresCreate(CreateView):
    model = CadastroDoadores
    fields = ['cpf', 'nome', 'sobrenome', 'dataNascimento', 'endereco', 'numero', 'bairro', 'cidade', 'telefonefixo',
              'celular', 'Intencao']
    template_name = 'formcaddoadores.html'
    success_url = reverse_lazy('index')


class QtDoacaoCreate(CreateView):
    model = QtDoacao
    fields = ['quantidade', 'descricao', 'd_cpf']
    template_name = 'formcaddoacao.html'
    success_url = reverse_lazy('index')
