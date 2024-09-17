from django import forms
from .models import Acessorio, Veiculo

class AcessorioForm(forms.ModelForm):
    class Meta:
        model = Acessorio
        fields = ['nome']

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

        label = {
        "modelo" : "Title",
        "anoFabricacao" : "Description",
        "placa": "Placa"
        }