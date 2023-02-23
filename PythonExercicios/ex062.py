termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
cont = 10
while cont != 0:
    print(f'[{termo}] ', end='')
    termo += razao
    if cont > 1:
        cont -= 1
    else:
        cont = int(input('\nQuer ver mais quantos termos? '))
