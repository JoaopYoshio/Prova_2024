from django.shortcuts import render, redirect
from .models import Veiculo, Acessorio
from .forms import AcessorioForm, VeiculoForm

def home(request):
    form = VeiculoForm
    veiculos = Veiculo.objects.all()
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VeiculoForm()
    return render(request, "index.html", {'form': form, "veiculos": veiculos})

def veiculos(request):
    return redirect('home')

def editar(request, id):
    veiculo = Veiculo.objects.get(id=id)   
    return render(request, "editar.html", {"veiculo": veiculo})

def salvar(request, id):   
    veiculo = Veiculo.objects.get(id=id)   
    veiculo.modelo = request.POST.get("modelo")
    veiculo.anoFabricacao = request.POST.get("anoFabricacao")
    veiculo.placa = request.POST.get("placa")
    veiculo.save()
    return redirect(home)

def deletar(resquet, id):
    veiculo = Veiculo.objects.get(id=id) 
    veiculo.delete()
    return redirect(home)

def adicionarAcessorio(request, id):
    veiculo = Veiculo.objects.get(id=id) 
    
    if request.method == 'POST':
        form = AcessorioForm(request.POST)
        if form.is_valid():
            acessorio = form.save(commit=False)
            acessorio.veiculo = veiculo
            acessorio.save()
    else:
        form = AcessorioForm()

    return render(request, 'addAcessorio.html', {'form': form, 'veiculo': veiculo})

def detalhesVeiculo(request, id):
    veiculo = Veiculo.objects.get(id=id) 

    if request.method == 'POST':
        form = AcessorioForm(request.POST)
        if form.is_valid():
            acessorio = form.save(commit=False)
            acessorio.veiculo = veiculo
            acessorio.save()
    else:
        form = AcessorioForm()

    acessorios = Acessorio.objects.filter(veiculo=veiculo)

    return render(request, 'detalhesVeiculo.html', {'form': form, 'veiculo': veiculo, 'acessorios': acessorios})

def deletarAcessorio(request, id):
    acessorio = Acessorio.objects.get(id=id) 
    veiculo_id = acessorio.veiculo.id 
    acessorio.delete()
    return redirect('detalhesVeiculo', id=veiculo_id)

