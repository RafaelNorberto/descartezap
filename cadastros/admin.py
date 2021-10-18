from django.contrib import admin

# Register your models here.

from .models import CadastroDoadores, QtDoacao

admin.site.register(CadastroDoadores)
admin.site.register(QtDoacao)