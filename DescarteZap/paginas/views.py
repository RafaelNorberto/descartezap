from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from DescarteZap.forms import CadAcessoForm

class PaginaInicial(TemplateView):
    template_name = "index.html"

class UsuarioCreate(CreateView):
    template_name = "templates/login.html"
    model = User
    fields = ['username', 'email', 'password']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de Novo Usuario"
        context['botao'] = "Cadastrar"

        return context


@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')

def logout_user(request):
    print(request.user)
    logout(request)
    return redirect('/login/')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha invalido. Favor tentar novamente')

    return redirect ('/login/')


