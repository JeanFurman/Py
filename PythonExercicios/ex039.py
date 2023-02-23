from datetime import date

ano = int(input('Qual o ano do seu nascimento: '))
new = date.today().year - ano
if new < 18:
    print(f'Voce ainda vai se alistar, faltam {18 - new} ano(s)')
elif new == 18:
    print(f'Esta na hora de se alistar!')
else:
    print(f'Voce passou do tempo de se alistar, {new - 18} ano(s) precisamente')
