from django.urls import path
from .views import pesquisa_view, pesquisa_concluida_view

urlpatterns = [
    path('', pesquisa_view, name='pesquisa_view'),
    path('concluido/', pesquisa_concluida_view, name='pesquisa_concluida'),
]
