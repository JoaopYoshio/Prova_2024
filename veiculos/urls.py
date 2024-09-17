from django.contrib import admin
from django.urls import path, include
from .views import home, salvar, editar, deletar

urlpatterns = [
    path('', home),
    path('salvar/', salvar, name="salvar"),
    path("editar/<int:id>/", editar, name="editar"),
    path('deletar/<int:id>/', deletar, name="deletar"),
    
]