from django.shortcuts import render, redirect
from .models import Pesquisa
from .forms import PesquisaForm  # Importe o formulário

def pesquisa_view(request):
    if request.method == "POST":
        form = PesquisaForm(request.POST)  # Preencha o formulário com os dados do POST
        if form.is_valid():  # Verifique se o formulário é válido
            form.save()  # Salve os dados no banco de dados
            return redirect('pesquisa_concluida')
    else:
        form = PesquisaForm()  # Crie um formulário vazio

    return render(request, 'pesquisa/formulario.html', {'form': form})

def pesquisa_concluida_view(request):
    return render(request, 'pesquisa/concluido.html')