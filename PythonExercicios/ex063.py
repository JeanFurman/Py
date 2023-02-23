n = int(input('Digite a quantidade de numeros da sequencia fibonacci: '))
soma = 0
aux = 1
aux2 = 0
while n > 0:
    print(f'[{soma}] ', end='')
    if soma == 0:
        soma = 1
    else:
        soma = aux + aux2
        aux2 = aux
        aux = soma
    n -= 1
