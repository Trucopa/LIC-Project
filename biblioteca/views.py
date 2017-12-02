from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Livro
from .models import Emprestimo

# Create your views here.

def livros_list(request):
    livros = Livro.objects.all()
    return render(request, 'biblioteca/livros_list.html', {'livros': livros})

def emprestimos_list(request):
    emprestimos = Emprestimo.objects.order_by('cliente')
    return render(request, 'biblioteca/emprestimos_list.html', {'emprestimos': emprestimos})

def emprestimo_detail(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    return render(request, 'biblioteca/emprestimo_detail.html', {'emprestimo': emprestimo})
