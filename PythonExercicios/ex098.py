from time import sleep


def contador(i, f, p):
    print('-=' * 25)
    if i < f:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        if p < 0:
            p = p * -1
        if p == 0:
            p = 1
        for k in range(i, f+1, p):
            print(f'{k} ', end='')
            sleep(0.5)
        print('FIM!')
    elif i == f:
        print('Valores invalidos, os numero sao iguais!')
    else:
        print(f'Contagem de {i} até {f} de {p if p != 0 else p + 1} em {p if p != 0 else p + 1}')
        if p > 0:
            p = p * -1
        if p == 0:
            p = -1
        for k in range(i, f - 1, p):
            print(f'{k} ', end='')
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 25)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))