from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.usuarios.models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    ordering = ('id',)

    list_display = ('id', 'email', 'nome_completo', 'is_active', 'is_superuser')
    list_filter = ('is_active', 'is_superuser')
    search_fields = ('email', 'nome_completo')

    add_fieldsets = fieldsets = (
        ('Credenciais', {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('nome_completo',)}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
