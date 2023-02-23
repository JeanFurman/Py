valores1 = list()
valores2 = list()
valores3 = list()
while True:
    valores1.append(int(input('Digite um numero: ')))
    r = ''
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
for c in valores1:
    if c % 2 == 0:
        valores2.append(c)
    else:
        valores3.append(c)
print('-=' * 30)
print(f'A lista completa é {valores1}')
print(f'A lista de pares é {valores2}')
print(f'A lista de impares é {valores3}')
