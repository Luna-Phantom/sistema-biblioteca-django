from django import forms
from datetime import datetime
from .models import Livro, Exemplar, Membro, Emprestimo, Reserva

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano']

    # FEATURE 2: Validação customizada do campo 'ano'
    def clean_ano(self):
        ano = self.cleaned_data.get('ano')
        ano_atual = datetime.now().year

        # Se o ano digitado for maior que o ano corrente, lança o erro de validação
        if ano and ano > ano_atual:
            raise forms.ValidationError(
                f"O ano de publicação ({ano}) não pode ser maior que o ano atual ({ano_atual})."
            )
        return ano


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