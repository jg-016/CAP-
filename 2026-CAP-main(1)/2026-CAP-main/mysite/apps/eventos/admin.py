from django.contrib import admin
from .models import *


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'calendario', 'inicio', 'fim')