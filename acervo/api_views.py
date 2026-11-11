from rest_framework import generics
from .models import Livro, Membro, Exemplar, Emprestimo, Reserva
from .serializers import (
    LivroSerializer, 
    MembroSerializer, 
    ExemplarSerializer, 
    EmprestimoSerializer, 
    ReservaSerializer
)

# função de segurança 
def org_atual(request):
    return request.user.perfil.organizacao

# --- LIVROS ---
class LivroListCreate(generics.ListCreateAPIView):
    serializer_class = LivroSerializer

    def get_queryset(self):
        org = org_atual(self.request)
        return Livro.objects.filter(organizacao=org)

    def perform_create(self, serializer):
        org = org_atual(self.request)
        serializer.save(organizacao=org) # Injeta a organização (equivalente ao commit=False)

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LivroSerializer

    def get_queryset(self):
        org = org_atual(self.request)
        return Livro.objects.filter(organizacao=org)

# --- MEMBROS ---
class MembroListCreate(generics.ListCreateAPIView):
    serializer_class = MembroSerializer

    def get_queryset(self):
        org = org_atual(self.request)
        return Membro.objects.filter(organizacao=org)

    def perform_create(self, serializer):
        org = org_atual(self.request)
        serializer.save(organizacao=org)

class MembroDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MembroSerializer

    def get_queryset(self):
        org = org_atual(self.request)
        return Membro.objects.filter(organizacao=org)

# --- EXEMPLARES ---
class ExemplarListCreate(generics.ListCreateAPIView):
    serializer_class = ExemplarSerializer

    def get_queryset(self):
        org = org_atual(self.request)
        return Exemplar.objects.filter(organizacao=org)

    def perform_create(self, serializer):
        org = org_atual(self.request)
        serializer.save(organizacao=org)

class ExemplarDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExemplarSerializer

    def get_queryset(self):
        org = org_atual(self.request)
        return Exemplar.objects.filter(organizacao=org)

# --- EMPRÉSTIMOS ---
class EmprestimoListCreate(generics.ListCreateAPIView):
    serializer_class = EmprestimoSerializer

    def get_queryset(self):
        org = org_atual(self.request)
        return Emprestimo.objects.filter(organizacao=org)

    def perform_create(self, serializer):
        org = org_atual(self.request)
        serializer.save(organizacao=org)

class EmprestimoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmprestimoSerializer

    def get_queryset(self):
        org = org_atual(self.request)
        return Emprestimo.objects.filter(organizacao=org)

# --- RESERVAS ---
class ReservaListCreate(generics.ListCreateAPIView):
    serializer_class = ReservaSerializer

    def get_queryset(self):
        org = org_atual(self.request)
        return Reserva.objects.filter(organizacao=org)

    def perform_create(self, serializer):
        org = org_atual(self.request)
        serializer.save(organizacao=org)

class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReservaSerializer

    def get_queryset(self):
        org = org_atual(self.request)
        return Reserva.objects.filter(organizacao=org)