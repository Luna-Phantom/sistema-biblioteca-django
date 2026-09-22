from django.contrib import admin
from .models import Emprestimo, Exemplar, Livro, Membro, Reserva

admin.site.register(Livro)
admin.site.register(Membro)
admin.site.register(Exemplar)
admin.site.register(Emprestimo)
admin.site.register(Reserva)