from django.urls import path
from .views import PaginaInicial

urlpatterns = [
    # path('endereco/', MinhaView.as_view(), 'name-da-url')
    path('', PaginaInicial.as_view(), name='index'),
]