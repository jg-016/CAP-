from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logout', views.logout_view, name='logout'),
    path('perfil', views.perfil, name='perfil')
]