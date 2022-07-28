from django.urls import path 
from . import views

urlpatterns = [
    path("genes", views.getGenes),
    path("genes/<int:id>", views.getGene)
]