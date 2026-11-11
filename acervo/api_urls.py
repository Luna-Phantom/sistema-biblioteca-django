from django.urls import path
from .api_views import (
    LivroListCreate, LivroDetail,
    MembroListCreate, MembroDetail,
    ExemplarListCreate, ExemplarDetail,
    EmprestimoListCreate, EmprestimoDetail,
    ReservaListCreate, ReservaDetail
)

urlpatterns = [
    # Rotas de Livros
    path('livros/', LivroListCreate.as_view()),
    path('livros/<int:pk>/', LivroDetail.as_view()),
    
    # Rotas de Membros
    path('membros/', MembroListCreate.as_view()),
    path('membros/<int:pk>/', MembroDetail.as_view()),
    
    # Rotas de Exemplares
    path('exemplares/', ExemplarListCreate.as_view()),
    path('exemplares/<int:pk>/', ExemplarDetail.as_view()),
    
    # Rotas de Empréstimos
    path('emprestimos/', EmprestimoListCreate.as_view()),
    path('emprestimos/<int:pk>/', EmprestimoDetail.as_view()),
    
    # Rotas de Reservas
    path('reservas/', ReservaListCreate.as_view()),
    path('reservas/<int:pk>/', ReservaDetail.as_view()),
]