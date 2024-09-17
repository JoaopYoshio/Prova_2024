from django.db import models


class Veiculo(models.Model):
    modelo = models.CharField(max_length=50)
    anoFabricacao = models.IntegerField()
    placa = models.CharField(max_length=20)

    def __str__(self):
        return self.modelo
    
class Acessorio(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

