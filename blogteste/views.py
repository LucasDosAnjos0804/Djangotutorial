"""
    SIMULA O CONTROLER, MAS TEM NOME DE VIEW
"""

from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    #busca os dados
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'blogteste/post_list.html',{'posts':posts})