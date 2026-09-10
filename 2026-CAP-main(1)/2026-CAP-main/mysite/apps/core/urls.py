from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('alterar_visibilidade_calendario/<int:id>', views.alterar_visibilidade_calendario, name='alterar_visibilidade_calendario'),
    path('alterar_visibilidade_turma/<int:id>', views.alterar_visibilidade_turma, name='alterar_visibilidade_turma'),
    path('semana_anterior', views.semana_anterior, name='semana_anterior'),
    path('proxima_semana', views.proxima_semana, name='proxima_semana'),
    path('voltar_para_hoje', views.voltar_para_hoje, name='voltar_para_hoje')
]

