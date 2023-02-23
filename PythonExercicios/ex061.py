termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
cont = 1
print(f'[{termo}] ', end='')
while cont < 10:
    termo += razao
    print(f'[{termo}] ', end='')
    cont += 1

