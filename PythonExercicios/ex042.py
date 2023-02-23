a = int(input('Numero 1: '))
b = int(input('Numero 2: '))
c = int(input('Numero 3: '))
triangulo = False
if a < (b + c) or b < (a + c) or c < (a + b):
    triangulo = True
if triangulo:
    if a == b == c:
        tipo = 'Equilatero'
    elif a != b != c != a:
        tipo = 'Escaleno'
    else:
        tipo = 'Isósceles'
    print(f'\033[33mÉ um triangulo {tipo}!')

else:
    print('Não é um triangulo!')


