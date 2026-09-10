from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.turmas.models import Turma, MembroDeTurma


@login_required
def turma(request, id):
    usuario = request.user
    turma = Turma.objects.get(id=id)
    context = {'turma': turma}
    return render(request, 'turmas/turma.html', context)


@login_required
def criar_turma(request):
    usuario = request.user

    numero_turma = 1
    while True:
        if not usuario.turmas.filter(nome__icontains=f'Turma {numero_turma}'):
            break
        numero_turma += 1
    nome_turma = f'Turma {numero_turma}'

    turma = Turma.objects.create(
        nome=nome_turma,
        descricao=f'Bem vindo a {nome_turma}!'
    )

    numero_paleta = usuario.paleta_menos_usada()

    MembroDeTurma.objects.create(
        usuario=usuario,
        turma=turma,
        eh_admin=True,
        numero_paleta=numero_paleta
    )

    return redirect('turma', turma.id)


@login_required
def atualizar_turma(request, id):
    usuario = request.user
    turma = Turma.objects.get(id=id)
    membro = MembroDeTurma.objects.get(usuario=usuario, turma=turma)

    if membro.eh_admin:
        ...

    return redirect('turma', id)


@login_required
def deletar_turma(request, id):
    usuario = request.user
    turma = Turma.objects.get(id=id)
    membro = MembroDeTurma.objects.get(usuario=usuario, turma=turma)

    if membro.eh_admin:
        turma.delete()
    else:
        raise ValueError('O usuário não é admin.')

    return redirect('inicio')