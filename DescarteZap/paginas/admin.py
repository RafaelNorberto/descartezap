from django.contrib import admin
from .models import CadastroDoadores

@admin.register(CadastroDoadores)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['id', 'bairro']

# Register your models here.
