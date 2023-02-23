from datetime import date
ano = int(input('Qual o ano de nascimento: '))
idade = date.today().year - ano
categoria = ''
if idade <= 9:
    categoria = 'Mirim'
elif 10 <= idade <= 14:
    categoria = 'Infantil'
elif 15 <= idade <= 19:
    categoria = 'Junior'
elif idade == 20:
    categoria = 'Senior'
else:
    categoria = 'Master'
print(f'Sua categoria é {categoria}')
