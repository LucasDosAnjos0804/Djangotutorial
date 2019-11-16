"""
    SIMULA O CONTROLER, MAS TEM NOME DE VIEW
    CONTROLA COMO AS INFORMACOES CAO EXIBIDAS E RECEBIDAS DOS "TEMPLATES"
"""

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    #busca os dados
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'blogteste/post_list.html',{'posts':posts})

def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)
    
    return render(request, 'blogteste/post_detail.html', {'post': post})