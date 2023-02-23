nota1 = float(input('Qual a sua 1 nota: '))
nota2 = float(input('Qual a sua 2 nota: '))

nota = (nota1 + nota2)/2
if nota < 5:
    print('BURRO BURRO BURRO')
elif 5 <= nota < 7:
    print('Recuperaçao!')
else:
    print('Aprovado!')