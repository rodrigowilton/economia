from django.shortcuts import render, redirect
from .models import Pesquisa

def pesquisa_view(request):
    if request.method == "POST":
        genero = request.POST.get('genero')
        idade = request.POST.get('idade')
        frequencia_compra = request.POST.get('frequencia_compra')
        gasto_medio = request.POST.get('gasto_medio')
        outras_lojas = request.POST.get('outras_lojas')
        principais_motivos = request.POST.get('principais_motivos')
        meios_deacompanhamento = request.POST.get('meios_deacompanhamento')
        canal_tv = request.POST.get('canal_tv')
        canal_radio = request.POST.get('canal_radio')
        uso_app = request.POST.get('uso_app')
        fatores_escolha = request.POST.get('fatores_escolha')
        motivos_redeconomia = request.POST.get('motivos_redeconomia')
        pontos_positivos = request.POST.get('pontos_positivos')
        pontos_negativos = request.POST.get('pontos_negativos')
        avaliacao_variedade = request.POST.get('avaliacao_variedade')
        avaliacao_limpeza = request.POST.get('avaliacao_limpeza')
        avaliacao_precos = request.POST.get('avaliacao_precos')
        produtos_anunciados = request.POST.get('produtos_anunciados')
        avaliacao_atendimento = request.POST.get('avaliacao_atendimento')
        sugestoes_melhorias = request.POST.get('sugestoes_melhorias')
        loja_redeconomia = request.POST.get('loja_redeconomia')

        Pesquisa.objects.create(
            genero=genero,
            idade=idade,
            frequencia_compra=frequencia_compra,
            gasto_medio=gasto_medio,
            outras_lojas=outras_lojas,
            principais_motivos=principais_motivos,
            meios_deacompanhamento=meios_deacompanhamento,
            canal_tv=canal_tv,
            canal_radio=canal_radio,
            uso_app=uso_app,
            fatores_escolha=fatores_escolha,
            motivos_redeconomia=motivos_redeconomia,
            pontos_positivos=pontos_positivos,
            pontos_negativos=pontos_negativos,
            avaliacao_variedade=avaliacao_variedade,
            avaliacao_limpeza=avaliacao_limpeza,
            avaliacao_precos=avaliacao_precos,
            produtos_anunciados=produtos_anunciados,
            avaliacao_atendimento=avaliacao_atendimento,
            sugestoes_melhorias=sugestoes_melhorias,
            loja_redeconomia=loja_redeconomia,
        )

        return redirect('pesquisa_concluida')

    return render(request, 'pesquisa/formulario.html', {'form': Pesquisa()})

def pesquisa_concluida_view(request):
    return render(request, 'pesquisa/concluido.html')