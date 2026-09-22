from django.shortcuts import render, redirect 
from .forms import ExemplarForm, LivroForm, MembroForm, EmprestimoForm, ReservaForm
from .models import Exemplar, Livro, Membro, Emprestimo, Reserva

def index(request):
  return render(request, 'acervo/index.html')

def lista_livros(request):
    livros = Livro.objects.all()
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