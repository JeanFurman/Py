print('-' * 30)
print('{: ^30}'.format('LOJA SUPER BARATAO'))
print('-' * 30)
preco = precoBarato = soma = cont = aux = 0
nome = nomeBarato = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += preco
    if preco > 1000:
        cont += 1
    if aux == 0:
        nomeBarato = nome
        precoBarato = preco
        aux = 1
    else:
        if preco < precoBarato:
            nomeBarato = nome
            precoBarato = preco
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeBarato} que custa R${precoBarato:.2f}')
