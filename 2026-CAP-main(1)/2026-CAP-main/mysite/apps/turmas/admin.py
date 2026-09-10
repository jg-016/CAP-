from django.contrib import admin
from .models import *


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'codigo', 'descricao')
    fieldsets = (
        (None, {'fields': ('nome', 'descricao')}),
    )


@admin.register(MembroDeTurma)
class MembroDeTurmaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'turma', 'eh_admin', 'numero_paleta')