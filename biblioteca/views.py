from django.shortcuts import render
from .models import Livro

# Create your views here.

def livros_list(request):
    livros = Livro.objects.all()
    return render(request, 'biblioteca/livros_list.html', {'livros': livros})
