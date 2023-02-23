valor = list()
for j in range(0, 5):
    n = int (input('Digite um valor: '))
    if j == 0 or n > max(valor):
        valor.append(n)
        print('Adicionado ao final da lista...')
    else:
        for k in range(0, len(valor)):
            if n <= valor[k]:
                valor.insert(k, n)
                print(f'Adicionado na posição {k} da lista...')
                break
print('-=' * 40)
print(f'Os valores digitados em ordem foram {valor}')
