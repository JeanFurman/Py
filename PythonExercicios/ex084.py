pessoas = list()
valores = []
maior = menor = aux = 0
while True:
    valores.append(str(input('Nome: ')))
    valores.append(float(input('Peso: ')))
    pessoas.append(valores[:])
    if aux == 0:
        maior = valores[1]
        menor = valores[1]
        aux = 1
    else:
        if menor > valores[1]:
            menor = valores[1]
        if maior < valores[1]:
            maior = valores[1]
    r = ' '
    valores.clear()
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar? [S/N] ')).upper()
    if r == 'N':
        break

print(f'Ao todo, voce cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for p in range(0, len(pessoas)):
    if pessoas[p][1] == maior:
        print(f'[{pessoas[p][0]}] ', end='')
print(f'\nO menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for p in range(0, len(pessoas)):
    if pessoas[p][1] == menor:
        print(f'[{pessoas[p][0]}] ', end='')

