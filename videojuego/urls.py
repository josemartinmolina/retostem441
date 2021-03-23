from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name = 'index'),
    path('proceso',views.proceso, name = 'proceso'),
    path('datos',views.datos, name = 'datos'),
]