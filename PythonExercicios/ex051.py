termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))

print(f'[{termo}] ', end='')
for j in range(0, 9):
    termo += razao
    print(f'[{termo}] ', end='')
