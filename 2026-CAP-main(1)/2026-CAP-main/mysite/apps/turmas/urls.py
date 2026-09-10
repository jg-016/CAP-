from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.turma, name='turma'),
    path('criar_turma', views.criar_turma, name='criar_turma'),
    path('atualizar_turma/<int:id>', views.atualizar_turma, name='atualizar_turma'),
    path('deletar_turma/<int:id>', views.deletar_turma, name='deletar_turma'),
]