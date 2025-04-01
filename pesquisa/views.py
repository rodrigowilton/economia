from django.shortcuts import render, redirect
from .forms import PesquisaForm
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from .models import Pesquisa
from django.db.models import Count

def gerar_grafico(request):
    # Recuperando os dados para o gráfico
    registros_por_entrevistadora = (
        Pesquisa.objects.values('colaboradora')
        .annotate(total=Count('colaboradora'))
        .order_by('colaboradora')
    )

    # Preparando dados para o gráfico
    entrevistadoras = [registro['colaboradora'] for registro in registros_por_entrevistadora]
    totais = [registro['total'] for registro in registros_por_entrevistadora]

    # Gerando o gráfico
    fig, ax = plt.subplots()
    ax.bar(entrevistadoras, totais)

    ax.set(xlabel='Entrevistadoras', ylabel='Total de Registros',
           title='Total de Registros por Entrevistadora')

    # Convertendo o gráfico para imagem em base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    gráfico_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    # Passando o gráfico para o contexto
    context = {
        'grafico': gráfico_base64,
    }

    return render(request, 'pesquisa/grafico.html', context)

def pesquisa_view(request):
    total_registros = Pesquisa.objects.count()
    registros_por_entrevistadora = Pesquisa.objects.values('colaboradora').annotate(total=Count('colaboradora'))

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

def pesquisa_satisfacao(request):
    total_registros = Pesquisa.objects.count()
    registros_por_entrevistadora = Pesquisa.objects.values('colaboradora').annotate(total=Count('colaboradora'))

    total_por_pergunta_por_loja = {}
    perguntas = [
        'genero', 'idade', 'frequencia_compra', 'gasto_medio', 'outras_lojas',
        'principais_motivos', 'meios_deacompanhamento', 'canal_tv', 'canal_radio',
        'uso_app', 'fatores_escolha', 'motivos_redeconomia', 'pontos_positivos',
        'pontos_negativos', 'avaliacao_variedade', 'avaliacao_limpeza', 'avaliacao_preços',
        'produtos_anunciados', 'avaliacao_atendimento', 'sugestoes_melhorias'
    ]

    for pergunta in perguntas:
        total_por_pergunta_por_loja[pergunta] = (
            Pesquisa.objects.values('loja_redeconomia', pergunta)
            .annotate(total=Count(pergunta))
            .order_by('loja_redeconomia', pergunta)
        )

    return render(request, 'pesquisa/totalizacao.html', {
        'total_registros': total_registros,
        'registros_por_entrevistadora': registros_por_entrevistadora,
        'total_por_pergunta_por_loja': total_por_pergunta_por_loja,
    })
