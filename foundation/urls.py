from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("automat_findEquationsAndSolve/", views.automat_findEquationsAndSolve, name="findEquationsAndSolve"),
]