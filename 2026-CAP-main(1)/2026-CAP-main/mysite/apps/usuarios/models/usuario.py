from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
import random

from apps.calendarios.models.membro_de_calendario import MembroDeCalendario
from apps.core.models import BaseModel
from apps.turmas.models.membro_de_turma import MembroDeTurma
from .usuario_manager import UsuarioManager


class Usuario(BaseModel, AbstractBaseUser, PermissionsMixin):
    # -------------------- FIELDS --------------------
    email = models.EmailField(unique=True)
    nome_completo = models.CharField(max_length=100)

    # -------------------- PERMISSÕES --------------------
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # -------------------- CONFIGURAÇÃO USUÁRIO --------------------
    objects: UsuarioManager = UsuarioManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome_completo"]

    def paleta_menos_usada(self) -> int:
        uso_de_paletas = {i:0 for i in range(1, 8)}

        for membro in MembroDeCalendario.objects.filter(usuario=self, calendario__turma=None):
            uso_de_paletas[membro.numero_paleta] += 1
        for membro in MembroDeTurma.objects.filter(usuario=self):
            uso_de_paletas[membro.numero_paleta] += 1

        menor_uso = min(uso_de_paletas.values())
        paletas_menos_usadas = [p for p in uso_de_paletas if uso_de_paletas[p] == menor_uso]
        paleta_menos_usada = random.choice(paletas_menos_usadas)

        return paleta_menos_usada

    def primeiro_nome(self) -> str:
        return self.nome_completo.split(' ')[0]

    def clean(self):
        if self.is_superuser and not self.is_staff:
            raise ValidationError("Superuser deve ter is_staff=True.")

    def __str__(self):
        return self.email