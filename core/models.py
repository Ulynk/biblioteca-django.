from django.db import models
from core.models import Categoria, Autor, Livro
from datetime import date


# Create your models here.
class Categoria(models.Model):
 nome = models.CharField(max_length=100)

def __str__(self):
 return self.nome

class Autor(models.Model):
 nome = models.CharField(max_length=100)

def __str__(self):
 return self.nome

class Livro(models.Model):
 titulo = models.CharField(max_length=200)
 autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
 categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
 publicado_em = models.DateField()

def __str__(self):
 return self.titulo

# Criando categorias
ficcao = Categoria.objects.create(nome='Ficção')
ciencia = Categoria.objects.create(nome='Ciência')

# Criando autores
asimov = Autor.objects.create(nome='Isaac Asimov')
sagan = Autor.objects.create(nome='Carl Sagan')

# Criando livros
Livro.objects.create(titulo='Fundação', autor=asimov,
categoria=ficcao, publicado_em=date(1951, 6, 1))
Livro.objects.create(titulo='Cosmos', autor=sagan, categoria=ciencia,
publicado_em=date(1980, 10, 1))

# Consulta de dados
ficcao_livros = Livro.objects.filter(categoria__nome='Ficção')
for livro in ficcao_livros:
 print(livro.titulo)

# Atualização de dados
fundacao = Livro.objects.get(titulo='Fundação')
fundacao.titulo = 'Fundação - Edição Revisada'
fundacao.save()

# Exclusão de dados
cosmos = Livro.objects.get(titulo='Cosmos')
cosmos.delete()