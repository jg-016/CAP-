from django.db import models
from django.db import IntegrityError
from apps.core.models import BaseModel
import string
import random


TAMANHO_CODIGO = 6
CARACTERES_CODIGO = string.ascii_letters + string.digits
def gerar_codigo_turma():
    return ''.join(random.choices(CARACTERES_CODIGO, k=TAMANHO_CODIGO))
    

class Turma(BaseModel):
    # -------------------- FIELDS --------------------
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500, blank=True)
    codigo = models.CharField(max_length=TAMANHO_CODIGO, unique=True, default=None)

    # -------------------- MANY TO MANY --------------------
    usuarios = models.ManyToManyField(
        to='usuarios.usuario',
        through='turmas.MembroDeTurma',
        related_name='turmas',
        related_query_name='turma'
    )

    def __init__(self, *args, **kwargs):
        if "codigo" in kwargs:
            raise TypeError("'codigo' de Turma é gerado automaticamente.")
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.codigo is None:
            for _ in range(20):
                try:
                    self.codigo = gerar_codigo_turma()
                    super().save(*args, **kwargs)
                    return 
                except IntegrityError:
                    continue
            raise ValueError("Não foi possível gerar código único")
        
    def __str__(self):
        return self.nome