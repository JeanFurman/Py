sexo = str(input('Digite um sexo valido [M, F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Sexo invalido! Digite um sexo valido [M, F]: ')).strip().upper()[0]
print(f'O sexo é {sexo}')
