from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("automat_findEquations/", views.automat_findEquations, name="findEquations"),
    path("automat_solveEquations/", views.automat_solveEquations, name="solveEquations"),
]