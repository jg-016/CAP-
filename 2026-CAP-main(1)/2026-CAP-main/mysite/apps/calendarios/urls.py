from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.calendario, name='calendario'),
    path('criar_calendario', views.criar_calendario, name='criar_calendario'),
    path('deletar_calendario/<int:id>', views.deletar_calendario, name='deletar_calendario'),
    path('atualizar_calendario/<int:id>', views.atualizar_calendario, name='atualizar_calendario')
]