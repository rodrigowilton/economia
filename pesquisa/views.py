from django.shortcuts import render, redirect
from .models import Pesquisa
from .forms import PesquisaForm
from django.db.models import Count

def pesquisa_view(request):
    total_registros = Pesquisa.objects.count()
    registros_por_entrevistadora = Pesquisa.objects.values('colaboradora').annotate(total=Count('colaboradora')).order_by('colaboradora')

    if request.method == "POST":
        form = PesquisaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pesquisa_concluida')
    else:
        form = PesquisaForm()

    return render(request, 'pesquisa/formulario.html', {
        'form': form,
        'total_registros': total_registros,
        'registros_por_entrevistadora': registros_por_entrevistadora
    })

def pesquisa_concluida_view(request):
    return render(request, 'pesquisa/concluido.html')