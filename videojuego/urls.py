from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name = 'index'),
    path('proceso',views.proceso, name = 'proceso'),
    path('datos',views.datos, name = 'datos'),
    path('unity',views.unity, name = 'unity'),
    path('buscaJugadorBody',views.buscaJugadorBody, name = 'buscaJugadorBody'),
    path('ejemploSQL', views.ejemploSQL, name='ejemploSQL'),
    path('score',views.score, name = 'score'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]