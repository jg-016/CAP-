
from datetime import date, datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from apps.eventos.models import Evento
from apps.calendarios.models import Calendario, MembroDeCalendario


MESES_ptbr = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril',
    'Maio', 'Junho', 'Julho', 'Agosto',
    'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]

DIAS_SEMANA_ptbr = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']


def get_dia_em_foco(request) -> date:
    dia_em_foco_str = request.session.setdefault(
        'dia_em_foco',
        timezone.localdate().isoformat()
    )
    return date.fromisoformat(dia_em_foco_str)


def set_dia_em_foco(request, dia_em_foco: date) -> None:
    request.session['dia_em_foco'] = dia_em_foco.isoformat()


def gerar_context_eventos_calendario_geral(
        request, 
        datas: list[date], 
        calendarios: list[Calendario]
):
    eventos_context = []

    calendarios_visiveis = []

    for calendario in calendarios:
        if calendario.id in request.session.get('calendarios_ocultos', []):
            continue

        if calendario.turma != None:
            if calendario.turma.id in request.session.get('turmas_ocultas', []):
                continue

        calendarios_visiveis.append(calendario)

    for calendario in calendarios_visiveis:
        membro_calendario = MembroDeCalendario.objects.get(
            calendario=calendario, 
            usuario=request.user
        )
        eventos = Evento.objects.filter(
            calendario=calendario, 
            inicio__date__in=[data.isoformat() for data in datas]
        )

        for evento in eventos:
            eventos_context.append( {
                'id': evento.id,
                'nome': evento.nome,
                'conteudo': evento.conteudo,
                'inicio': evento.inicio,
                'fim': evento.fim,
                'calendario_id': calendario.id,
                'paleta': membro_calendario.numero_paleta
            } )
        
    return eventos_context

@login_required
def inicio(request):
    dia_em_foco = get_dia_em_foco(request)
    mes_em_foco = MESES_ptbr[dia_em_foco.month - 1]
    ano_em_foco = dia_em_foco.year

    dias_ate_domingo = (dia_em_foco.weekday() + 1) % 7
    ultimo_domingo = dia_em_foco - timedelta(days=dias_ate_domingo)

    datas_calendario_geral = []

    for i in range(7):
        data = ultimo_domingo + timedelta(days=i)
        nome = f'{DIAS_SEMANA_ptbr[data.weekday()]} {data.day:02}'

        datas_calendario_geral.append( {
            'nome': nome,
            'isoformat': data.isoformat(),
        } )

    horarios_calendario_geral = [f'{i:02}:00'for i in range(24)]

    eventos = gerar_context_eventos_calendario_geral(
        request=request,
        datas=[ultimo_domingo + timedelta(i) for i in range(7)],
        calendarios=request.user.calendarios.all()
    )

    context = {
        'dia_em_foco': dia_em_foco,
        'mes_em_foco': mes_em_foco,
        'ano_em_foco': ano_em_foco,
        'datas_calendario_geral': datas_calendario_geral,
        'horarios_calendario_geral': horarios_calendario_geral,
        'eventos': eventos
    }

    return render(request, 'core/inicio.html', context)


def semana_anterior(request):    
    dia_em_foco = get_dia_em_foco(request)
    set_dia_em_foco(request, dia_em_foco - timedelta(days=7))
    return redirect('inicio')


def proxima_semana(request):
    dia_em_foco = get_dia_em_foco(request)
    set_dia_em_foco(request, dia_em_foco + timedelta(days=7))
    return redirect('inicio')


def voltar_para_hoje(request):
    set_dia_em_foco(request, timezone.localdate())
    return redirect('inicio')