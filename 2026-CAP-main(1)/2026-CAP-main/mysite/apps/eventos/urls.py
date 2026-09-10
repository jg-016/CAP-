from django.urls import path
from .views import criar_evento, deletar_evento, visualizar_evento

app_name = 'eventos'

urlpatterns = [
    path('criar/', criar_evento, name='criar_evento'),
    path('<int:id>/', visualizar_evento, name='visualizar_evento'),
    path('<int:id>/deletar/', deletar_evento, name='deletar_evento'),
]
