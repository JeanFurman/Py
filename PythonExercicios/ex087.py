matriz = [[], [], []]
par = soma = maior = 0
for k in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para [{k, j}]: '))
        matriz[k].append(n)
print('-=' * 30)
for k in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[k][j]}:^5]', end='')
    print('\n', end='')
print('-=' * 30)
for k in range(0, 3):
    for j in range(0, 3):
        if matriz[k][j] % 2 == 0:
            par += matriz[k][j]
    soma += matriz[k][2]
    if matriz[1][k] > maior:
        maior = matriz[1][k]
print(f'A soma dos valores pares e {par}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior numero da segunda linha é {maior}')


