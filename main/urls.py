from django.contrib import admin
from django.urls import path, include
from . import views

app_main = "main"

urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('observacao/', views.formulario, name="observaçao")
]