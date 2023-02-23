km = float(input('Velocidade: '))

if km > 80:
    multa = (km - 80)*7
    print(f'Voce foi multado ,o valor da sua multa é R${multa:.0f}')
else:
    print('Sem multa pro ce!')