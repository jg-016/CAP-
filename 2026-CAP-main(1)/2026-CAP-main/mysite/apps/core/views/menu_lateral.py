from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def alterar_visibilidade_calendario(request, id):
    calendarios_ocultos = request.session.setdefault('calendarios_ocultos', [])
    if id in calendarios_ocultos:
        calendarios_ocultos.remove(id)
    else:
        calendarios_ocultos.append(id)

    request.session.modified = True
    return redirect(request.GET.get("next", "inicio"))


@login_required
def alterar_visibilidade_turma(request, id):
    turmas_ocultas = request.session.setdefault('turmas_ocultas', [])
    if id in turmas_ocultas:
        turmas_ocultas.remove(id)
    else:
        turmas_ocultas.append(id)
    
    request.session.modified = True
    return redirect(request.GET.get("next", "inicio"))