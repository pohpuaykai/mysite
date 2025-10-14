from django.urls import path

from . import views

urlpatterns = [
    path("circuitAnimeRecord/", views.circuitAnimeRecord, name="circuitAnimeRecord"),
    path("basic_findEquations_audioFiles/", views.basic_findEquations_audioFiles, name="basic_findEquations_audioFiles"),
    path("basic_solvingSteps_audioFiles/", views.basic_solvingSteps_audioFiles, name="basic_solvingSteps_audioFiles"),
    path("wavFiles/", views.wavFiles, name="wavFiles"),
]