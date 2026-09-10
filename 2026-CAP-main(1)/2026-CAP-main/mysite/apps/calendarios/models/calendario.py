from django.db import models
from apps.core.models import BaseModel


class Calendario(BaseModel):
    # -------------------- FIELDS --------------------
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500, blank=True)

    # -------------------- FOREIGN KEY --------------------
    turma = models.ForeignKey(
        to='turmas.Turma',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='calendarios',
        related_query_name='calendario'
    )

    # -------------------- MANY TO MANY --------------------
    usuarios = models.ManyToManyField(
        to='usuarios.usuario',
        through='calendarios.MembroDeCalendario',
        related_name='calendarios',
        related_query_name='calendario'
    )

    def __str__(self):
        return f"{self.nome}/{self.turma}"