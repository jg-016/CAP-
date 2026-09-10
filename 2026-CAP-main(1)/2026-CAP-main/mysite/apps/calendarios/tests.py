from datetime import datetime, timedelta

from django.test import TestCase
from django.urls import reverse

from apps.calendarios.models import Calendario, MembroDeCalendario
from apps.eventos.models import Evento
from apps.usuarios.models import Usuario


class CalendarioViewTests(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            email='teste@teste.com',
            password='Senha@123',
            nome_completo='Usuário Teste',
        )
        self.calendario = Calendario.objects.create(
            nome='Calendário Teste',
            descricao='Descrição do calendário',
        )
        MembroDeCalendario.objects.create(
            usuario=self.usuario,
            calendario=self.calendario,
            eh_admin=True,
            numero_paleta=1,
        )

    def test_calendario_exibe_visualizacao_semanal(self):
        evento = Evento.objects.create(
            nome='Reunião do grupo',
            conteudo='Planejamento da semana',
            inicio=datetime(2026, 8, 12, 9, 0, 0),
            fim=datetime(2026, 8, 12, 10, 30, 0),
            calendario=self.calendario,
        )

        self.client.force_login(self.usuario)
        response = self.client.get(reverse('calendario', args=[self.calendario.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'calendar-week-view')
        self.assertContains(response, evento.nome)

    def test_criar_evento_redireciona_para_o_calendario(self):
        self.client.force_login(self.usuario)
        response = self.client.post(
            reverse('eventos:criar_evento'),
            {
                'titulo': 'Nova tarefa',
                'calendario': self.calendario.id,
                'data': '2026-08-12',
                'inicio': '09:00',
                'fim': '10:00',
                'descricao': 'Descrição da tarefa',
            },
        )

        self.assertRedirects(response, reverse('calendario', args=[self.calendario.id]))
        self.assertTrue(
            Evento.objects.filter(
                calendario=self.calendario,
                nome='Nova tarefa',
            ).exists()
        )
