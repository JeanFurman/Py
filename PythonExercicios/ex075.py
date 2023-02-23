a = b = c = d = cont = 0

for j in range(0, 4):
    e = int(input('Digite um numero: '))
    if cont == 0:
        a = e
    elif cont == 1:
        b = e
    elif cont == 2:
        c = e
    elif cont == 3:
        d = e
    cont += 1
tupla = (a, b, c, d)
print(f'Voce digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)}')
try:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1} posiçao')
except ValueError:
    print(f'O valor 3 não foi digitado em nenhuma posiçao')
print('Os valores pares digitados foram ', end='')
for k in tupla:
    if k % 2 == 0:
        print(f'{k} ', end='')
