from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

from apps.core.models import BaseModel
from datetime import datetime


DATA_EVENTO_MINIMA = datetime(2000, 1, 1, 0, 0, 0)
DATA_EVENTO_MAXIMA = datetime(2050, 12, 31, 23, 59, 59)


class Evento(BaseModel):
    # -------------------- FIELDS --------------------
    nome = models.CharField(max_length=100)
    conteudo = models.CharField(max_length=500, blank=True)
    inicio = models.DateTimeField(
        validators=[
            MinValueValidator(DATA_EVENTO_MINIMA),
            MaxValueValidator(DATA_EVENTO_MAXIMA)
        ]
    )
    fim = models.DateTimeField(
        validators=[
            MinValueValidator(DATA_EVENTO_MINIMA),
            MaxValueValidator(DATA_EVENTO_MAXIMA)
        ]
    )

    # -------------------- FOREIGN KEYS --------------------
    calendario = models.ForeignKey(
        to='calendarios.Calendario',
        on_delete=models.CASCADE,
        related_name='eventos',
        related_query_name='evento'
    )

    def clean(self):
        if self.inicio.day != self.fim.day:
            raise ValidationError('O inicio e fim do evento devem ser no mesmo dia.')

        if self.inicio >= self.fim:
            raise ValidationError('O fim do evento não pode vir antes do inicio.',)

    def __str__(self):
        return self.nome