"""
    CONTROLA AS URL's E DESIGNA A "VIEW" CORRESPONDENTE
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    ## O primeiro argumento se trata do padrão da url com nome post_detail, observe <int:pk> que dizer que o Django espera em seguidao do '/' um numero inteiro e irá trasnferi-lo para view(controlador) como uma variavel chamada pk.
    ## O segundo argumento eh a funcao disparada em view.
    ## O terceiro argumento eh o nome da view.
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
