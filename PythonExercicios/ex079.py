valor = list()
continuar = ' '
while True:
    n = int(input('Digite um valor: '))
    if n in valor:
        print('Valor duplicado! Nao vou adicionar...')
    else:
        valor.append(n)
        print('Valor adicionado com sucesso...')
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
    continuar = ' '

valor.sort()
print(f'Voce digitou os valores {valor}')
