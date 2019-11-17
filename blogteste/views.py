"""
    SIMULA O CONTROLER, MAS TEM NOME DE VIEW
    CONTROLA COMO AS INFORMACOES CAO EXIBIDAS E RECEBIDAS DOS "TEMPLATES"
"""

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
    #busca os dados
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    #retorna render, funcao http, o diretorio do tamplate, mensagem ao template
    return render(request,'blogteste/post_list.html',{'posts':posts})

def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)
    
    return render(request, 'blogteste/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blogteste/post_edit.html', {'form': form})

def post_edit(request, pk):
     post = get_object_or_404(Post, pk=pk)
     if request.method == "POST":
         form = PostForm(request.POST, instance=post)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date = timezone.now()
             post.save()
             return redirect('post_detail', pk=post.pk)
     else:
         form = PostForm(instance=post)
     return render(request, 'blogteste/post_edit.html', {'form': form})



