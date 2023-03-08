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