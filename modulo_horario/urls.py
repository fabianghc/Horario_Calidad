from django.urls import path
from . import views
from modulo_ambiente import *

urlpatterns = [
    path('', views.inicio),
    path('horario/', views.horario),
    path('menuHorario/', views.menuHorario),
    path('menuCurso/', views.menuCurso),
    path('menuDocente/', views.menuDocente),
    path('menuAmbiente/', views.menuAmbiente)
]