from rest_framework import serializers
from datetime import datetime
from .models import Livro, Membro, Exemplar, Emprestimo, Reserva

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'ano', 'disponivel']

    def validate_ano(self, value):
        ano_atual = datetime.now().year
        if value and value > ano_atual:
            raise serializers.ValidationError(
                f"O ano de publicação ({value}) não pode ser maior que o ano atual ({ano_atual})."
            )
        return value

class MembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membro
        fields = ['id', 'nome', 'email', 'telefone']

class ExemplarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exemplar
        fields = ['id', 'livro', 'codigo_tombamento', 'disponivel']

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['id', 'exemplar', 'membro', 'data_emprestimo', 'data_devolucao_prevista', 'data_devolucao_real', 'multa']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'livro', 'membro', 'data_reserva', 'ativa']