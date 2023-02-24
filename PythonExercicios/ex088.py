from random import randint
from time import sleep
jogos = list()
palpites = list()
print('-' * 40)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-' * 40)
n = int(input('Quantos jogos voce quer que eu sorteie? '))
print('{:^30}'.format(f' SORTEANDO {n} JOGOS '))
for k in range(0, n):
    for j in range(0, 6):
        r = randint(1, 60)
        if j == 0:
            palpites.append(r)
        else:
            while True:
                if r not in palpites:
                    break
                r = randint(1, 60)
            palpites.append(r)
    jogos.append(palpites[:])
    palpites.clear()
for k in range(0, n):
    print(f'Jogo {k+1}: {sorted(jogos[k])}')
    sleep(1)
print('{:^30}'.format('< BOA SORTE! >'))
