from django.urls import path

from . import views

urlpatterns = [
    path("circuitAnimeRecord/", views.circuitAnimeRecord, name="circuitAnimeRecord"),
]