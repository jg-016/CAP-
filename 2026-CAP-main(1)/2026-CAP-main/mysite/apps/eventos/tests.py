from django.test import TestCase
from django.urls import reverse
from datetime import datetime

from apps.calendarios.models import Calendario, MembroDeCalendario
from apps.usuarios.models import Usuario

from .models import Evento


class EventoViewTests(TestCase):
	def setUp(self):
		self.usuario = Usuario.objects.create_user(
			email='admin@teste.com',
			password='Senha@123',
			nome_completo='Administrador',
		)
		self.calendario = Calendario.objects.create(nome='Calendário teste')
		MembroDeCalendario.objects.create(
			usuario=self.usuario,
			calendario=self.calendario,
			eh_admin=True,
			numero_paleta=1,
		)
		self.evento = Evento.objects.create(
			nome='Reunião',
			conteudo='Planejamento',
			inicio=datetime(2026, 8, 12, 9, 0),
			fim=datetime(2026, 8, 12, 10, 0),
			calendario=self.calendario,
		)
		self.client.force_login(self.usuario)

	def test_visualizar_evento_exibe_informacoes(self):
		response = self.client.get(
			reverse('eventos:visualizar_evento', args=[self.evento.id])
		)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, self.evento.nome)
		self.assertContains(response, self.evento.conteudo)
		self.assertContains(response, 'Deletar evento')

	def test_deletar_evento_remove_evento_e_redireciona(self):
		response = self.client.post(
			reverse('eventos:deletar_evento', args=[self.evento.id])
		)

		self.assertRedirects(
			response,
			reverse('calendario', args=[self.calendario.id]),
		)
		self.assertFalse(Evento.objects.filter(id=self.evento.id).exists())

	def test_membro_comum_nao_pode_deletar_evento(self):
		membro = Usuario.objects.create_user(
			email='membro@teste.com',
			password='Senha@123',
			nome_completo='Membro',
		)
		MembroDeCalendario.objects.create(
			usuario=membro,
			calendario=self.calendario,
			eh_admin=False,
			numero_paleta=2,
		)
		self.client.force_login(membro)

		response = self.client.post(
			reverse('eventos:deletar_evento', args=[self.evento.id])
		)

		self.assertRedirects(
			response,
			reverse('eventos:visualizar_evento', args=[self.evento.id]),
		)
		self.assertTrue(Evento.objects.filter(id=self.evento.id).exists())
