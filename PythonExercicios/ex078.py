lista = list()
for j in range(0, 5):
    lista.append(int(input(f'Digite um valor para posiçao {j} :')))
print(f'Voce digitou os valores {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi {maior} nas posiçoes ', end='')
for pos, c in enumerate(lista):
    if c == maior:
        print(f'{pos}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posiçoes ', end='')
for pos, c in enumerate(lista):
    if c == menor:
        print(f'{pos}... ', end='')


