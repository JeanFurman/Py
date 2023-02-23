print('=' * 30)
print('          BANCO CEV        ')
print('=' * 30)
c50 = c20 = c10 = c01 = 0

valor = int(input('Que valor voce quer sacar? R$'))
c50 = valor // 50
aux = c50 * 50
c20 = (valor % 50)//20
aux += c20 * 20
c10 = (valor - aux)//10
aux += c10 * 10
c01 = (valor - aux)//1

if c50 > 0:
    print(f'Total de {c50} cédulas de R$50')
if c20 > 0:
    print(f'Total de {c20} cédulas de R$20')
if c10 > 0:
    print(f'Total de {c10} cédulas de R$10')
if c01 > 0:
    print(f'Total de {c01} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
