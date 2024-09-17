from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, deletar, veiculos, deletarAcessorio, detalhesVeiculo

urlpatterns = [
    path('', home, name="home"),
    path('', veiculos, name="veiculos"),
    path("editar/<int:id>/", editar, name="editar"),
    path("salvar/<int:id>/", salvar, name="salvar"),
    path('deletar/<int:id>/', deletar, name="deletar"),
    path('detalhesVeiculo/<int:id>/', detalhesVeiculo, name='detalhesVeiculo'),
    path('deletarAcessorio/<int:id>/', deletarAcessorio, name='deletarAcessorio'),
]