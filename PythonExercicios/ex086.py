matriz = [[], [], []]
for k in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para [{k, j}]: '))
        matriz[k].append(n)
print('-=' * 30)
for k in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[k][j]:^5}]', end='')
    print('\n', end='')
