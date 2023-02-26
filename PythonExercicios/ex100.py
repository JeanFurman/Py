from random import randint
from time import sleep


def sorteia(n):
    print('Sorteando 5 valores da lista: ', end='')
    for k in range(0, 5):
        n.append(randint(1, 10))
        print(f'{n[k]} ', end='')
        sleep(0.5)
    print('PRONTO!')
    somaPar(n)


def somaPar(num):
    print(f'Somando os valores pares de {num}, temos ', end='')
    soma = 0
    for n in num:
        if n % 2 == 0:
            soma += n
    print(soma)


numeros = list()
sorteia(numeros)
