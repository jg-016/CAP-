from django.core.exceptions import ValidationError  
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from apps.usuarios.models.usuario import Usuario


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip()
        password = request.POST.get('password')

        usuario = authenticate(request, email=email, password=password)

        if usuario is None:
            erro = 'email ou senha inválidos.'
            return render(request, 'usuarios/login.html', {'erro': erro})
        else:
            login(request, usuario)
            return redirect('inicio')

    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def cadastro(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip()
        nome_completo = request.POST.get('nome_completo').strip()
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if password1 != password2:
            erro = 'Digite a mesma senha!'
            return render(request, 'usuarios/cadastro.html', {'erro': erro})
            
        try:
            Usuario.objects.create_user(
                email=email,
                password=password1,
                nome_completo=nome_completo
            )   
        except ValidationError as e:
            return render(request, "usuarios/cadastro.html", {"erro": e.messages[0]})
        except Exception as e:
            return render(request, "usuarios/cadastro.html", {"erro": str(e)})

        return redirect('login')

    return render(request, 'usuarios/cadastro.html')
