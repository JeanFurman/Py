listagem = ('Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25,
            'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-' * 50)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print('{:.<50}'.format(listagem[c]), end='')
    else:
        print('R${:>7}'.format(listagem[c]))
print('-' * 50)
