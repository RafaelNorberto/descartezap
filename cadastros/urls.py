from django.urls import path
from .views import CadastroDoadoresCreate, QtDoacaoCreate
#  define a url para chamar a pagina

urlpatterns = [
    # formato para definir url

    path('cadastrar/cadastrodoadores/', CadastroDoadoresCreate.as_view(), name='cadastrar-doador'),
    path('cadastrar/qtdoacao/', QtDoacaoCreate.as_view(), name='cadastrar-doacao'),

]