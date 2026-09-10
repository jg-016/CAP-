from datetime import datetime

from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from apps.calendarios.models import Calendario
from apps.calendarios.models import MembroDeCalendario
from apps.eventos.models import Evento


@login_required
def criar_evento(request):
    if request.method == 'POST':

        titulo = request.POST.get('titulo', '').strip()
        data = request.POST.get('data')
        inicio = request.POST.get('inicio')
        fim = request.POST.get('fim')
        descricao = request.POST.get('descricao', '').strip()
        calendario = Calendario.objects.filter(
            usuarios=request.user,
            turma=None
        ).first()

        if not calendario:
            calendario = Calendario.objects.create(
                nome='Calendário geral',
                descricao='Calendário geral do usuário'
            )

            MembroDeCalendario.objects.create(
                usuario=request.user,
                calendario=calendario,
                eh_admin=True,
                numero_paleta=request.user.paleta_menos_usada(),
            )
        if titulo and data and inicio and fim:

            try:
                inicio_dt = datetime.fromisoformat(
                    f'{data}T{inicio}'
                )
                fim_dt = datetime.fromisoformat(
                    f'{data}T{fim}'
                )
                evento = Evento(
                    nome=titulo,
                    conteudo=descricao,
                    inicio=inicio_dt,
                    fim=fim_dt,
                    calendario=calendario,
                )
                evento.full_clean()
                evento.save()
            except (ValueError, ValidationError):
                pass
    return redirect('calendario', id=calendario.id)


@login_required
def visualizar_evento(request, id):
    evento = get_object_or_404(
        Evento.objects.select_related('calendario'),
        id=id,
        calendario__usuarios=request.user,
    )
    membro = get_object_or_404(
        MembroDeCalendario,
        calendario=evento.calendario,
        usuario=request.user,
    )

    return render(
        request,
        'eventos/visualizar_evento.html',
        {'evento': evento, 'usuario_eh_admin': membro.eh_admin},
    )


@login_required
def deletar_evento(request, id):
    evento = get_object_or_404(
        Evento.objects.select_related('calendario'),
        id=id,
        calendario__usuarios=request.user,
    )
    membro = get_object_or_404(
        MembroDeCalendario,
        calendario=evento.calendario,
        usuario=request.user,
    )

    if not membro.eh_admin:
        return redirect('eventos:visualizar_evento', id=evento.id)

    if request.method == 'POST':
        calendario_id = evento.calendario_id
        evento.delete()
        return redirect('calendario', id=calendario_id)

    return render(request, 'eventos/deletar_evento.html', {'evento': evento})
