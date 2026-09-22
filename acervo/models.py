from django.db import models
from django.utils import timezone

class Livro(models.Model):
  titulo = models.CharField(max_length=200)
  autor = models.CharField(max_length=100)
  ano = models.IntegerField()
  disponivel = models.BooleanField(default=True)

  def __str__(self):
    return self.titulo


class Membro(models.Model):
  nome = models.CharField(max_length=150)
  email = models.EmailField(unique=True)
  telefone = models.CharField(max_length=20)

  def __str__(self):
    return self.nome


class Exemplar(models.Model):
  livro = models.ForeignKey(
      Livro, on_delete=models.CASCADE, related_name='exemplares'
  )
  codigo_tombamento = models.CharField(max_length=50, unique=True)
  disponivel = models.BooleanField(default=True)

  def __str__(self):
    return f'{self.livro.titulo} - Exemplar: {self.codigo_tombamento}'

class Emprestimo(models.Model):
  exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE)
  membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
  data_emprestimo = models.DateField(default=timezone.localdate)
  data_devolucao_prevista = models.DateField()
  data_devolucao_real = models.DateField(null=True, blank=True)
  multa = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

  def __str__(self):
    return f'Empréstimo: {self.exemplar.livro.titulo} para {self.membro.nome}'


class Reserva(models.Model):
  livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
  membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
  data_reserva = models.DateTimeField(auto_now_add=True)
  ativa = models.BooleanField(default=True)

  def __str__(self):
    return f'Reserva: {self.livro.titulo} por {self.membro.nome}'