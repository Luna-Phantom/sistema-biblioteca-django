import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import (
    ExemplarForm, LivroForm, MembroForm, EmprestimoForm, ReservaForm, PeriodoForm
)
from .models import Exemplar, Livro, Membro, Emprestimo, Reserva
from .dashboard import obter_dados_dashboard, filtrar_periodo

def index(request):
    return render(request, 'acervo/index.html')

# --- FEATURE 1: BUSCA E FILTRO NA LISTAGEM DE LIVROS ---
def lista_livros(request):
    livros = Livro.objects.all()
    
    # Captura os parâmetros enviados via GET na URL (Requisito técnico)
    busca = request.GET.get('q', '').strip()
    ano_filtro = request.GET.get('ano', '').strip()

    # 1. Busca por texto (Título OU Autor) usando Q() - Desafio Extra
    if busca:
        livros = livros.filter(
            Q(titulo__icontains=busca) | Q(autor__icontains=busca)
        )

    # 2. Filtro por Ano de publicação (se informado no select)
    if ano_filtro:
        livros = livros.filter(ano=ano_filtro)

    return render(request, 'acervo/lista.html', {'livros': livros})

def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = LivroForm()
    return render(request, 'acervo/form.html', {'form': form})

# --- MEMBROS ---
def lista_membros(request):
    membros = Membro.objects.all()
    return render(request, 'acervo/lista_membros.html', {'membros': membros})

def novo_membro(request):
    if request.method == 'POST':
        form = MembroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_membros')
    else:
        form = MembroForm()
    return render(request, 'acervo/form_membro.html', {'form': form})

# --- EXEMPLARES ---
def lista_exemplares(request):
    exemplares = Exemplar.objects.all()
    return render(request, 'acervo/lista_exemplares.html', {'exemplares': exemplares})

def novo_exemplar(request):
    if request.method == 'POST':
        form = ExemplarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_exemplares')
    else:
        form = ExemplarForm()
    return render(request, 'acervo/form_exemplar.html', {'form': form})

# --- EMPRÉSTIMOS ---
def lista_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(
        request, 'acervo/lista_emprestimos.html', {'emprestimos': emprestimos}
    )

def novo_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_emprestimos')
    else:
        form = EmprestimoForm()
    return render(request, 'acervo/form_emprestimo.html', {'form': form})

# --- RESERVAS ---
def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'acervo/lista_reservas.html', {'reservas': reservas})

def nova_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()
    return render(request, 'acervo/form_reserva.html', {'form': form})

# --- DASHBOARD E RELATÓRIOS (P2) ---
@login_required
def dashboard(request):
    perfil = request.user.perfil
    dados = obter_dados_dashboard(perfil.organizacao, request)
    
    contexto = {
        **dados,
        'form': PeriodoForm(request.GET),
        'mostra_series': perfil.eh_admin,  # Admin vê gráfico e CSV; Operador não[cite: 71]
        'org': perfil.organizacao,
        'perfil': perfil,
    }
    return render(request, 'acervo/dashboard.html', contexto)

@login_required
def dashboard(request):
    perfil = request.user.perfil
    dados = obter_dados_dashboard(perfil.organizacao, request)
    
    contexto = {
        **dados,
        'form': PeriodoForm(request.GET),
        'mostra_series': perfil.eh_admin,
        'org': perfil.organizacao,
        'perfil': perfil,
    }
    return render(request, 'acervo/dashboard.html', contexto)

@login_required
def exportar_csv(request):
    perfil = request.user.perfil
    if not perfil.eh_admin:
        return HttpResponseForbidden("Acesso negado: apenas administradores podem exportar relatórios.")

    qs = filtrar_periodo(
        request,
        Emprestimo.objects.filter(organizacao=perfil.organizacao)
        .select_related('exemplar__livro', 'membro')
    )

    resp = HttpResponse(content_type='text/csv; charset=utf-8')
    resp['Content-Disposition'] = 'attachment; filename="relatorio_emprestimos.csv"'
    
    w = csv.writer(resp)
    w.writerow(['Livro', 'Exemplar', 'Membro', 'Data Empréstimo', 'Devolução Real'])
    
    for e in qs:
        w.writerow([
            e.exemplar.livro.titulo,
            str(e.exemplar),
            str(e.membro),
            e.data_emprestimo,
            e.data_devolucao_real or 'Em aberto',
        ])
    return resp