from django.shortcuts import render

# Create your views here.

def livros_list(request):
    return render(request, 'biblioteca/livros_list.html', {})
