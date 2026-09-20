from django.db import models


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