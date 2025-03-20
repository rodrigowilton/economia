from django.urls import path, include

urlpatterns = [
    path('pesquisa/', include('pesquisa.urls')),
]
