from django.db import models


class BaseModel(models.Model):
    # -------------------- FIELDS --------------------
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True