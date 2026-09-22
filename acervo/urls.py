from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('livros/', views.lista_livros, name='lista'),
    path('livros/novo/', views.novo_livro, name='novo_livro'),
    path('membros/', views.lista_membros, name='lista_membros'),
    path('membros/novo/', views.novo_membro, name='novo_membro'),
    path('exemplares/', views.lista_exemplares, name='lista_exemplares'),
    path('exemplares/novo/', views.novo_exemplar, name='novo_exemplar'),
    path('emprestimos/', views.lista_emprestimos, name='lista_emprestimos'),
    path('emprestimos/novo/', views.novo_emprestimo, name='novo_emprestimo'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/nova/', views.nova_reserva, name='nova_reserva'),
]