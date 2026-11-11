from rest_framework import generics
from .models import Livro, Membro, Exemplar, Emprestimo, Reserva
from .serializers import (
    LivroSerializer, 
    MembroSerializer, 
    ExemplarSerializer, 
    EmprestimoSerializer, 
    ReservaSerializer
)

# --- LIVROS ---
class LivroListCreate(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

# --- MEMBROS ---
class MembroListCreate(generics.ListCreateAPIView):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer

class MembroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer

# --- EXEMPLARES ---
class ExemplarListCreate(generics.ListCreateAPIView):
    queryset = Exemplar.objects.all()
    serializer_class = ExemplarSerializer

class ExemplarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exemplar.objects.all()
    serializer_class = ExemplarSerializer

# --- EMPRÉSTIMOS ---
class EmprestimoListCreate(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class EmprestimoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

# --- RESERVAS ---
class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer