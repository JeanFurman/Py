km = float(input('Quantos kilometros: '))

if km <= 200:
    print(f'O preço é: R${km * 0.50:.2f}')
else:
    print(f'O preço é: R${km * 0.45}')
