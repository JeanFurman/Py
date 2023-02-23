soma = 0
for j in range(0, 6):
    n = int(input(f'Numero {j+1}: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos numeros pares é: {soma}')
