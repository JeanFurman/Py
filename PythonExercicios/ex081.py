valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    r = ''
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
valores.sort(reverse=True)
print(f'Voce digitou {len(valores)} elementos')
print(f'Os valores em ordem decrescente sao {valores}')
print('O valor 5 faz parte da lista' if 5 in valores else 'O valor 5 nao foi encontrado na lista')
