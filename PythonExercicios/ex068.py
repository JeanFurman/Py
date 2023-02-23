from random import randint
cont = 0
print('=-' * 40)
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    print('=-' * 40)
    player = int(input('Diga um valor: '))
    par = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    cpu = randint(0, 11)
    if (player + cpu) % 2 == 0:
        r = 0
    else:
        r = 1
    string = ['PAR', 'ÍMPAR']
    print('-' * 40)
    print(f'Voce jogou {player} e o computador {cpu}. Total de {player + cpu} DEU {string[r]}')
    print('-' * 40)
    if r == 0 and par == 'P' or r == 1 and par == 'I':
        print('Voce VENCEU!')
        print('Vamod jogar novamente...')
        cont += 1
    else:
        break
print('Voce PERDEU!')
print('=-' * 40)
print(f'GAME OVER! Voce venceu {cont} vezes.')