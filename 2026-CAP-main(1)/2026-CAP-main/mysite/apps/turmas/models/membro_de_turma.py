from django.db import models
from django.core.validators import MaxValueValidator
from apps.core.models import BaseModel


class MembroDeTurma(BaseModel):
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
    turma = models.ForeignKey(
        to='turmas.Turma', 
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'turma'],
                name='unique_usuario_turma'
            )
        ]
    
    def __str__(self):
        return f'{self.usuario.email} de {self.turma.nome}'
    
    