from django.core import management
from pathlib import Path
from django.conf import settings

from apps.usuarios.models import Usuario
from apps.turmas.models import Turma, MembroDeTurma
from apps.calendarios.models import Calendario, MembroDeCalendario
from apps.eventos.models import Evento

from .dados_populate import (
    dados_usuarios,
    dados_turmas,
    dados_calendarios,
)


def resetar_banco():
    db: Path = settings.BASE_DIR / 'db_development.sqlite3'

    if db.exists():
        db.unlink()

    management.call_command('migrate')


def popular_usuarios(dados_usuarios):
    for dados in dados_usuarios:
        Usuario.objects.create_superuser(**dados)


def popular_turmas(dados_turmas):
    for dados in dados_turmas:
        dados_calendarios = dados.pop('calendarios', [])
        numero_paleta = dados.pop('numero_paleta', 1)
        descricao = f'Bem vindo a {dados['nome']}!'

        turma = Turma.objects.create(descricao=descricao, **dados)
        popular_calendarios(dados_calendarios, turma=turma, numero_paleta=numero_paleta)

        for usuario in Usuario.objects.all():
            MembroDeTurma.objects.create(
                usuario=usuario,
                turma=turma,
                eh_admin=True,
                numero_paleta=numero_paleta
            )


def popular_calendarios(dados_calendarios, *, turma=None, numero_paleta=1):
    for dados in dados_calendarios:
        dados_eventos = dados.pop('eventos', [])
        _numero_paleta = dados.pop('numero_paleta', numero_paleta)
        _turma = dados.pop('turma', turma)
        descricao = dados.pop('descricao', f'Bem vindo a {dados['nome']}!')

        calendario = Calendario.objects.create(**dados, turma=_turma, descricao=descricao)
        popular_eventos(dados_eventos, calendario=calendario)

        for usuario in Usuario.objects.all():
            MembroDeCalendario.objects.create(
                usuario=usuario,
                calendario=calendario,
                eh_admin=True if usuario.primeiro_nome() not in ['Alexandre', 'André'] else False,
                numero_paleta=_numero_paleta
            )


def popular_eventos(dados_eventos, *, calendario):
    for dados in dados_eventos:
        conteudo = dados.pop('conteudo', f'Este é o evento de nome {dados['nome']}!')
        Evento.objects.create(**dados, calendario=calendario, conteudo=conteudo)


class Command(management.base.BaseCommand):
    help = "Popula o banco com dados de desenvolvimento."

    def handle(self, *args, **options):
        while True:
            resposta = input(self.style.ERROR('Esta ação vai limpar o banco. Continuar mesmo assim? [s/n] '))
            if resposta.strip() == 's': break
            if resposta.strip() == 'n': return

        self.stdout.write("Limpando banco...")
        resetar_banco()

        self.stdout.write("Criando usuários...")
        popular_usuarios(dados_usuarios) 
    
        self.stdout.write("Criando turmas...")
        popular_turmas(dados_turmas)

        self.stdout.write("Criando calendários...")
        popular_calendarios(dados_calendarios)

        self.stdout.write(self.style.SUCCESS("Banco populado com sucesso!"))