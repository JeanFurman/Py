from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
aux = 0
maior = 0
menor = 0
print('Os valores sorteados foram: ', end='')
for c in num:
    print(f'{c} ', end='')
    if aux == 0:
        maior = c
        menor = c
    else:
        if maior < c:
            maior = c
        if menor > c:
            menor = c
    aux = 1
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
