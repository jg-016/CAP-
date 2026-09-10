from apps.calendarios.models import Calendario
from apps.calendarios.models import MembroDeCalendario
from apps.turmas.models import MembroDeTurma
from apps.turmas.models.turma import Turma


def _get_dados_calendario(request, calendario: Calendario) -> dict:
    try:
        membro = MembroDeCalendario.objects.get(
            usuario=request.user,
            calendario=calendario
        )
    except MembroDeCalendario.DoesNotExist:
        return {}

    calendarios_ocultos = request.session.get('calendarios_ocultos', [])
    turmas_ocultas = request.session.get('turmas_ocultas', [])

    botao_menu_preenchido = calendario.id not in calendarios_ocultos

    eventos_visiveis = (
        calendario.id not in calendarios_ocultos
        and (
            calendario.turma is None
            or calendario.turma.id not in turmas_ocultas
        )
    )

    return {
        'id': calendario.id,
        'nome': calendario.nome,
        'descricao': calendario.descricao,
        'paleta': membro.numero_paleta,
        'eventos_visiveis': eventos_visiveis,
        'botao_menu_preenchido': botao_menu_preenchido,
        'turma': calendario.turma
    }


def _get_dados_turma(request, turma: Turma) -> dict:
    try:
        membro_turma = MembroDeTurma.objects.get(
            usuario=request.user,
            turma=turma
        )
    except MembroDeTurma.DoesNotExist:
        return {}

    calendarios_de_turma = []

    for calendario in turma.calendarios.all():
        dados_calendario = _get_dados_calendario(request, calendario)

        if dados_calendario:
            calendarios_de_turma.append(dados_calendario)

    turmas_ocultas = request.session.get('turmas_ocultas', [])

    botao_menu_preenchido = turma.id not in turmas_ocultas
    eventos_visiveis = turma.id not in turmas_ocultas

    return {
        'id': turma.id,
        'nome': turma.nome,
        'descricao': turma.descricao,
        'paleta': membro_turma.numero_paleta,
        'eventos_visiveis': eventos_visiveis,
        'botao_menu_preenchido': botao_menu_preenchido,
        'calendarios': calendarios_de_turma
    }


def get_dados_calendarios_sem_turma(request):
    if not request.user.is_authenticated:
        return {'calendarios_sem_turma': []}

    dados_calendarios = []

    for calendario in request.user.calendarios.filter(turma=None):
        dados_calendario = _get_dados_calendario(request, calendario)

        if dados_calendario:
            dados_calendarios.append(dados_calendario)

    return {'calendarios_sem_turma': dados_calendarios}


def get_dados_turmas(request):
    if not request.user.is_authenticated:
        return {'turmas': []}

    dados_turmas = []

    for turma in request.user.turmas.all():
        dados_turma = _get_dados_turma(request, turma)

        if dados_turma:
            dados_turmas.append(dados_turma)

    return {'turmas': dados_turmas}