from django.views.generic import TemplateView


# definição da pagina inicial
class IndexView(TemplateView):
    template_name = "index.html"


# definição da pagina inicial
class SobreView(TemplateView):
    template_name = "paginas/sobre.html"