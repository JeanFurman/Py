numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

escolha = int(input('Digite um numero entre 0 e 20: '))
while True:
    if 0 < escolha <= 20:
        break
    escolha = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print(f'Voce digitou o numero {numeros[escolha]}')
