parada = 'S'
soma = maior = menor = cont = 0
while parada == 'S':
    n = int(input('Digite um numero: '))
    parada = str(input('Quer continuar? [S]/[N]\n')).upper()
    soma += n
    cont += 1
    if maior == 0:
        maior = n
    elif maior < n:
        maior = n
    if menor == 0:
        menor = n
    elif menor > n:
        menor = n
print(f'A media dos valores digitados é {soma / cont}\nO Maior numero é {maior} e o Menor numero é {menor}')
