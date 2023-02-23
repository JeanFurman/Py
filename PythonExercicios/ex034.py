sal = float(input('Digite o salario: '))

if sal > 1250:
    print(f'O salario com aumento será R${sal + (sal * 10/100):.2f}!')
else:
    print(f'O salario com aumento será R${sal + (sal * 15 / 100):.2f}!')