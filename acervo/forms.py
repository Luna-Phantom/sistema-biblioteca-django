from django import forms
from .models import Livro, Exemplar, Membro, Emprestimo, Reserva

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano']

class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ['nome', 'email', 'telefone']


class ExemplarForm(forms.ModelForm):
    class Meta:
        model = Exemplar
        fields = ['livro', 'codigo_tombamento', 'disponivel']

class EmprestimoForm(forms.ModelForm):

  class Meta:
    model = Emprestimo
    fields = ['exemplar', 'membro', 'data_devolucao_prevista']
    widgets = {
        'data_devolucao_prevista': forms.DateInput(attrs={'type': 'date'}),
    }


class ReservaForm(forms.ModelForm):

  class Meta:
    model = Reserva
    fields = ['livro', 'membro']