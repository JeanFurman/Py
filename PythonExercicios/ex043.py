peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura**2

if imc <= 18.5:
    status = 'Abaixo do peso'
elif 18.5 < imc <= 25:
    status = 'Peso ideal'
elif 25 < imc <= 30:
    status = 'Sobrepeso'
elif 30 < imc <= 40:
    status = 'Obesidade'
else:
    status = 'Obesidade mórbida'
print(f'IMC: {imc:.1f} - {status}')

