from django.contrib import admin
from .models import Exemplar, Livro, Membro

admin.site.register(Livro)
admin.site.register(Membro)
admin.site.register(Exemplar)