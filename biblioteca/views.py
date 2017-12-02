from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Livro
from .models import Emprestimo
from .forms import EmprestimoForm
from .forms import LivroForm
from django.shortcuts import redirect

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

def emprestimo_new(request):
    if request.method == "POST":
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.save()
            return redirect('emprestimo_detail', pk=emprestimo.pk)
    else:
        form = EmprestimoForm()
    return render(request, 'biblioteca/emprestimo_edit.html', {'form': form})


def livro_new(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            livro.save()
            return redirect('emprestimos_list')
    else:
        form = LivroForm()
    return render(request, 'biblioteca/livro_edit.html', {'form': form})
