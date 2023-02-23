n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))

if n1 > n2 and n1 > n3:
    print(f'O numero {n1} é o maior!')
else:
    if n2 > n1 and n2 > n3:
        print(f'O numero {n2} é o maior!')
    else:
        print(f'O numero {n3} é o maior')

if n1 < n2 and n1 < n3:
    print(f'O numero {n1} é o menor!')
else:
    if n2 < n1 and n2 < n3:
        print(f'O numero {n2} é o menor!')
    else:
        print(f'O numero {n3} é o menor!')
