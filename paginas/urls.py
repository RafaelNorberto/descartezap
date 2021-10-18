from django.urls import path
from .views import IndexView, SobreView


#  define a url para chamar a pagina

urlpatterns = [
    # formato para definir url
    # path('endereço/', 'MinhaView.as_views()', name='endereço da url'),
    path('inicio/', IndexView.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]