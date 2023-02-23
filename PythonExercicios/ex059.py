menu = 0
while menu != 5:
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    r = int(input('''[1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR
    Escolha a opção: '''))
    if r == 1:
        print(f'A soma de {n1} e {n2} é {n1+n2}')
    elif r == 2:
        print(f'A multiplicaçao de {n1} e {n2} é {n1 * n2}')
    elif r == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior numero entre {n1} e {n2} é {maior}')
    elif r == 5:
        menu = 5
