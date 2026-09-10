from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def perfil(request):
    context = {}
    return render(request, 'usuarios/perfil.html', context)