from django.db import migrations

def org_padrao(apps, schema_editor):
    Org = apps.get_model('core', 'Organizacao')
    Livro = apps.get_model('acervo', 'Livro')
    Membro = apps.get_model('acervo', 'Membro')
    Exemplar = apps.get_model('acervo', 'Exemplar')
    Emprestimo = apps.get_model('acervo', 'Emprestimo')
    Reserva = apps.get_model('acervo', 'Reserva')

    # Cria a organização padrão
    org, created = Org.objects.get_or_create(nome='Biblioteca Padrão')

    # Atualiza todos os registros vazios
    Livro.objects.filter(organizacao__isnull=True).update(organizacao=org)
    Membro.objects.filter(organizacao__isnull=True).update(organizacao=org)
    Exemplar.objects.filter(organizacao__isnull=True).update(organizacao=org)
    Emprestimo.objects.filter(organizacao__isnull=True).update(organizacao=org)
    Reserva.objects.filter(organizacao__isnull=True).update(organizacao=org)

class Migration(migrations.Migration):

    dependencies = [
        ('acervo', '0004_emprestimo_organizacao_exemplar_organizacao_and_more'),
    ]

    operations = [
        migrations.RunPython(org_padrao, migrations.RunPython.noop)
    ]