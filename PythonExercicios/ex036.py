casa = float(input('Qual o valor da casa: '))
sal = float(input('Qual o seu salario: '))
ano = int(input('Quantos anos: '))

emp = casa / (12 * ano)
if emp > sal * 30/100:
    print('Negado!')
else:
    print(f'Aprovado! o valor da parcela é {emp:.2f}')