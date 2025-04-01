from django.urls import path
from .views import pesquisa_view, pesquisa_concluida_view, pesquisa_satisfacao,gerar_grafico,pesquisa_grafico_view

urlpatterns = [
    path('', pesquisa_view, name='pesquisa_view'),
    path('concluido/', pesquisa_concluida_view, name='pesquisa_concluida'),
    path('totalizacao/', pesquisa_satisfacao, name='pesquisa_satisfacao'),
    path('grafico2/', gerar_grafico, name='grafico'),  # URL para o gráfico
    path('grafico/', pesquisa_grafico_view, name='pesquisa_grafico'),

]
