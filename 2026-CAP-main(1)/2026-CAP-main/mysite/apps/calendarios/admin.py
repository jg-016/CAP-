from django.contrib import admin
from .models import *


@admin.register(Calendario)
class CalendarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'turma', 'descricao')


@admin.register(MembroDeCalendario)
class MembroDeCalendarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'calendario', 'eh_admin', 'numero_paleta')