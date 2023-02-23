soma = 0
aux = 0
cont = 0
while aux != 999:
    aux = int(input('Digite um numero: '))
    if aux != 999:
        soma += aux
        cont += 1
print(f'A soma foi de {soma} e a quantidade de numeros digitados é {cont}!')
