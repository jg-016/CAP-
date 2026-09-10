from apps.calendarios.models import Calendario


def get_calendarios(request):
    """Context processor que retorna todos os calendários.

    Mantém a chave do contexto como `calendarios` para compatibilidade
    com os templates existentes.
    """
    return {
        'calendarios': Calendario.objects.all(),
    }
