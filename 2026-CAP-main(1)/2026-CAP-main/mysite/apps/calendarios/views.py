import json
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.calendarios.models import Calendario
from apps.calendarios.models.membro_de_calendario import MembroDeCalendario


@login_required
def calendario(request, id):
    usuario = request.user

    calendario = Calendario.objects.get(id=id)

    membro = MembroDeCalendario.objects.get(
        usuario=usuario,
        calendario=calendario
    )

    membros_calendario = MembroDeCalendario.objects.filter(
        calendario=calendario
    )

    lideres = [
        {
            'nome': membro.usuario.nome_completo,
            'email': membro.usuario.email
        }
        for membro in membros_calendario.filter(eh_admin=True)
    ]

    membros_comuns = [
        {
            'nome': membro.usuario.nome_completo,
            'email': membro.usuario.email
        }
        for membro in membros_calendario.filter(eh_admin=False)
    ]

    eventos = calendario.eventos.all().order_by('inicio')

    eventos_json = json.dumps([
        {
            'id': evento.id,
            'title': evento.nome,
            'description': evento.conteudo,
            'date': evento.inicio.strftime('%Y-%m-%d'),
            'start': evento.inicio.hour + evento.inicio.minute / 60,
            'end': evento.fim.hour + evento.fim.minute / 60,
            'detail_url': reverse(
                'eventos:visualizar_evento', args=[evento.id]
            ),
        }
        for evento in eventos
    ])

    calendario_context = {
        'id': calendario.id,
        'nome': calendario.nome,
        'descricao': calendario.descricao,
        'turma': calendario.turma,
        'lideres': lideres,
        'membros_comuns': membros_comuns,
        'eventos': eventos,
        'eventos_json': eventos_json,
    }

    usuario_context = {
        'nome': request.user.nome_completo,
        'email': request.user.email,
        'eh_admin': membro.eh_admin,
        'paleta': membro.numero_paleta,
    }

    context = {
        'calendario': calendario_context,
        'usuario': usuario_context
    }

    return render(
        request,
        'calendarios/calendario.html',
        context
    )


# COLOQUE A FUNÇÃO AQUI
@login_required
def criar_calendario(request):
    usuario = request.user

    numero_calendario = 1

    while True:
        if not usuario.calendarios.filter(
            turma=None,
            nome__icontains=f'Calendário {numero_calendario}'
        ):
            break

        numero_calendario += 1

    nome_calendario = f'Calendário {numero_calendario}'

    calendario = Calendario.objects.create(
        nome=nome_calendario,
        descricao=f'Bem vindo a {nome_calendario}!'
    )

    numero_paleta = usuario.paleta_menos_usada()

    MembroDeCalendario.objects.create(
        usuario=usuario,
        calendario=calendario,
        eh_admin=True,
        numero_paleta=numero_paleta
    )

    return redirect('calendario', calendario.id)


@login_required
def atualizar_calendario(request, id):
    usuario = request.user

    calendario = Calendario.objects.get(id=id)

    membro = MembroDeCalendario.objects.get(
        usuario=usuario,
        calendario=calendario
    )

    if membro.eh_admin:
        ...

    return redirect('calendario', id)


@login_required
def deletar_calendario(request, id):
    usuario = request.user

    calendario = Calendario.objects.get(id=id)

    membro = MembroDeCalendario.objects.get(
        usuario=usuario,
        calendario=calendario
    )

    if membro.eh_admin:
        calendario.delete()
    else:
        raise ValueError('O usuário não é admin.')

    return redirect('inicio')