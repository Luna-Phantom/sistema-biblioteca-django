# Sistema de Biblioteca 📚

Projeto desenvolvido em **Django** (padrão MVT) para gerenciar uma biblioteca acadêmica. O sistema conta com controle completo de livros, membros, exemplares, empréstimos, reservas e uma regra de negócio para cálculo automático de multas por atraso na devolução.

---

## 🚀 Passo a passo para rodar na hora da prova

Se precisar baixar o projeto do GitHub e colocá-lo para rodar em um computador novo, abra o terminal na pasta desejada e siga esta sequência:

1. **Baixar o projeto do GitHub:**
 ```bash
 git clone https://github.com/Luna-Phantom/sistema-biblioteca-django.git
 cd <nome-da-pasta-do-projeto>
   ```
2. **Criar um ambiente virtual**
```
python -m venv venv
.\venv\Scripts\Activate
```
3. **Instalar o Django**
```
pip install django
```
4.**Criar o banco de dados(migrações)**
```
python manage.py makemigrations
python manage.py migrate
```
5.**Criar seu usuário administrador (para o /admin):**
```
python manage.py createsuperuser
```
6.**Rodar o servidor**
```
python manage.py runserver
```
