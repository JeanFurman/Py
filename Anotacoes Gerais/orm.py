lives_like = Live.objects.filter(like_lte=1000) lte = menor/igual
lives_like.count()

lives_python = Live.objects.filter(title_icontains='python')
live_python.count()
for live in lives_python:
	print(live.number, live.title)

lives_no_python = Live.objects.exclude(title_icontains='python')
lives_no_python.count()

Live.objects.filter(like__lte=1000).values('title', 'guest__first_name') //return dicionario

Live.objects.filter(like__lte=1000).values_list('title', 'guest') // return tupla

Live.objects.filter(like__lte=1000).values_list('title', flat=True) // return list mas pra somente 1 item

Live.objects.filter(title__icontains='python', guest__first_name__icontains='rafael')

Live.objects.filter(Q(title__icontains='django') | Q(guest__first_name__icontains='andr'))

from django.db import connection

lives = Live.objects.all()
for live in lives:
	print(live.guest)

print(len(connection.queries))

lives = Live.objects.select_related('guest').all() // query otimizada
for live in lives:
	print(live.guest)

print(len(connection.queries))

lives = Live.objects.all()

print(lives.query) // return a query SQL


lives = [
	'Testes de unidade na pratica',
	'Melhorando teste de unidade',
	'Testando o que esta pronto',
	'Autenticaçao de uma API Flask com testes',
	'BDD com python e flask',
	'Type hints e Anotaçoes de funçoes',
	'Django basico',
	'Django parte 2',
]

for i, live in enumerate(lives):
	Live.objects.create(title=live, number=i)

print(len(connection.queries)) // 8 vezes no banco

aux=[]
for i, live in enumerate(lives):
	obj = Live(title=live, number=i)
	aux.append(obj)

Live.objects.bulk_create(aux)

print(len(connection.queries)) // 2 só

words = ['Testes de unidade na pratica', 'Melhorando teste de unidade']

Live.objects.filter(title__in=words).count() // return 2

Live.objects.filter(title__in=words).distinct()

Live.objects.all().values_list('like', flat=True).order_by('-like')

Programador.objects.filter(nome__iexact='Jean') //tras exatamente o valor i=ignorecase

Programador.objects.filter(nome__startswith='n')//tras a primeira letra i=ignorecase

Programador.objects.filter(nome__iendswith='n')//tras a ultima letra i=ignorecase

Programador.objects.filter(nome__in=['jean', 'davi'])//tras os nomes (se existirem) do banco 

Programador.objects.filter(salario__gt=1000)//maior que 1000 

Programador.objects.filter(salario__gte=1000)//maior igual a 1000 

Programador.objects.filter(salario__lt=1000)//menor que 1000 

Programador.objects.filter(salario__lte=1000)//maior igual a 1000 

Programador.objects.filter(empresa__isnull=True/False) retorna se o campo é nulo ou não

ProgramadorLinguagem.objects.filter(programador__nome__icontains='th', linguagem__nome='Python')

busca = Q(
			Q(nome='jean') | Q(nome='davi')
		)

Programador.objects.filter(busca)

busca = Q(
			Q(nome__contains='a') & Q(salario__gt=3000)
		)

Programador.objects.filter(busca)

busca = Q(
			Q(

				Q(nome__contains='a') & Q(salario__gt=3000)
			)
			&
			Q(empresa__nome='Google')
		)

User.objects.get(email='jean@gmail.com')

from django.db.models.aggregates import Avg, Sum, Count, Min, Max

Livro.objects.aggregate(avaliacao_media=Avg('avaliacao'), preco_medio=Avg('preco'), 
	mais_caro=Max('preco'), mais_bem_avaliado=Max('avaliacao'))

Livro.objects.filter(categoria='Drama').aggregate(avaliacao_media=Avg('avaliacao'), preco_medio=Avg('preco'), 
	mais_caro=Max('preco'), mais_bem_avaliado=Max('avaliacao'))

autores = Autor.objects.annotate(nota_media=Avg('livros__avaliacao'))

for autor in autores:
	print(f'Nome: {autor.nome} - Nota média: {autor.nota_media}')

autores = Autor.objects.filter(idade__gt=55).annotate(nota_media=Avg('livros__avaliacao'))

for autor in autores:
	print(f'Nome: {autor.nome} - Nota média: {autor.nota_media}')

Livro.objects.values('categoria').annotate(nota_media=Avg('avaliacao'))

from django.db.models import F

Livro.objects.filter(categoria='Terror').update(preco=F('preco')*1.25)

programadores = Programador.objects.all().select_related('empresa') //OneToOne ou ForeignKey

programadores = Programador.objects.all().prefetch_related('linguagens') //ManyToMany

programadores = Programador.objects.all().select_related('empresa').only('empresa__nome') // tras só o nome e economiza espaço na memoria

programadores = Programador.objects.all().select_related('empresa').defer('empresa__nome')// exclui esse dado da pesquisa e economiza espaço na memoria

