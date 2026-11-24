from django.db.models import Count, Q
from django.db.models.functions import TruncMonth
from .models import Emprestimo
from .forms import PeriodoForm

def filtrar_periodo(request, qs):
    form = PeriodoForm(request.GET)
    if form.is_valid():
        if form.cleaned_data.get('inicio'):
            qs = qs.filter(data_emprestimo__gte=form.cleaned_data['inicio'])
        if form.cleaned_data.get('fim'):
            qs = qs.filter(data_emprestimo__lte=form.cleaned_data['fim'])
    return qs

def obter_dados_dashboard(org, request=None):
    # Base sempre filtrada pela organização e otimizada contra N+1
    base = Emprestimo.objects.filter(organizacao=org).select_related('exemplar__livro', 'membro')
    
    if request:
        base = filtrar_periodo(request, base)

    # 1. KPIs (Totais)
    kpis = base.aggregate(
        total=Count('id'),
        membros_ativos=Count('membro', distinct=True),
        em_aberto=Count('id', filter=Q(data_devolucao_real__isnull=True))
    )

    # 2. Ranking (Top 5 livros mais emprestados)
    ranking = list(
        base.values('exemplar__livro__titulo')
        .annotate(total=Count('id'))
        .order_by('-total')[:5]
    )

    # 3. Série Temporal (Empréstimos por mês)
    por_mes_qs = (
        base.annotate(mes=TruncMonth('data_emprestimo'))
        .values('mes')
        .annotate(total=Count('id'))
        .order_by('mes')
    )
    por_mes = [
        {'mes': r['mes'].strftime('%m/%Y'), 'total': r['total']}
        for r in por_mes_qs if r['mes']
    ]

    # 4. Distribuição (Devolvidos vs Em aberto)
    devolvidos = kpis['total'] - kpis['em_aberto']
    distribuicao = [
        {'status': 'Devolvidos', 'total': devolvidos},
        {'status': 'Em Aberto', 'total': kpis['em_aberto']}
    ]

    return {
        'kpis': kpis,
        'ranking': ranking,
        'por_mes': por_mes,
        'distribuicao': distribuicao,
    }