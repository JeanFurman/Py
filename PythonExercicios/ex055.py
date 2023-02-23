maior = 0.0
menor = 0.0
for j in range(0, 5):
    peso = float(input(f'Digite o {j+1} peso: '))
    if j == 0:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
print(f'Maior peso {maior} | Menor peso: {menor}')
