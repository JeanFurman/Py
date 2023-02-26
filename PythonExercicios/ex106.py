from time import sleep


def linhas(s, *num):
    print(f'\033[{num[0]};{num[1]}m', end='')
    print('~' * (len(s) + 4))
    print(f'  {s}')
    print('~' * (len(s) + 4))
    print('\033[m', end='')


while True:
    linhas('SISTEMA DE AJUDA PyHELP', 107, 42)
    f = str(input('Funçao ou biblioteca > ')).lower()
    if f == 'fim':
        break
    linhas(f"Acessando o manual do comando '{f}'", 107, 44)
    sleep(2)
    print('\033[30;107m', end='')
    print(f'{help(f)}'[:-4], end='')
    print('\033[m', end='')
    sleep(2)
linhas('ATE LOGO!', 107, 41)
