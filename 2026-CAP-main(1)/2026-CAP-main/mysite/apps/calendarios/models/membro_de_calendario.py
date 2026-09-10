from django.db import models
from django.core.validators import MaxValueValidator
from apps.core.models import BaseModel


class MembroDeCalendario(BaseModel):
    # -------------------- FIELDS --------------------
    eh_admin = models.BooleanField()
    numero_paleta = models.PositiveIntegerField(
        validators = [MaxValueValidator(9)]
    )

    # -------------------- FOREIGN KEYS --------------------
    usuario = models.ForeignKey(
        to='usuarios.Usuario', 
        on_delete=models.CASCADE
    )
    calendario = models.ForeignKey(
        to='calendarios.Calendario', 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.usuario.email} de {self.calendario.nome}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'calendario'],
                name='unique_usuario_calendario'
            )
        ]