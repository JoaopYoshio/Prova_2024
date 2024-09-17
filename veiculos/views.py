from django.shortcuts import render, redirect
from .models import Veiculo

def home(request):
    veiculos = Veiculo.objects.all()
    return render(request, "index.html", {"veiculos": veiculos})

def salvar(request):   
    _modelo = request.POST.get("modelo")
    _anoFabricacao = request.POST.get("anoFabricacao")
    _placa = request.POST.get("placa")
    Veiculo.objects.create(modelo=_modelo, anoFabricacao=_anoFabricacao, placa=_placa)
    veiculos = Veiculo.objects.all()
    return render(request, "index.html", {"veiculos": veiculos})

def editar(request, id):
    veiculo = Veiculo.objects.get(id=id)   
    _modelo = request.POST.get("modelo")
    _anoFabricacao = request.POST.get("anoFabricacao")
    _placa = request.POST.get("placa")
    return redirect(home)

def deletar(resquet, id):
    veiculo = Veiculo.objects.get(id=id) 
    veiculo.delete()
    return redirect(home)



