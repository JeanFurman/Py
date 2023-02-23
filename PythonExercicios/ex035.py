a = int(input('Numero 1: '))
b = int(input('Numero 2: '))
c = int(input('Numero 3: '))
triangulo = False
if a > b and a > c:
    if a < (b + c):
        triangulo = True
else:
    if b > a and b > c:
        if b < (a + c):
            triangulo = True
    else:
        if c > a and c > b:
            if c < (a + b):
                triangulo = True
        else:
            if a == b and a == c:
                triangulo = True
if triangulo:
    print('\033[33mÉ um triangulo!')
else:
    print('Não é um triangulo!')


