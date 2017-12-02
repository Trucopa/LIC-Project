from django import forms

from .models import Emprestimo
from .models import Livro

class EmprestimoForm(forms.ModelForm):

    class Meta:
        model = Emprestimo
        fields = ('cliente', 'livro')


class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = ('autor', 'titulo','isbn','editora')
