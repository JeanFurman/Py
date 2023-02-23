from datetime import date
maior = 0
menor = 0
for j in range(0, 7):
    ano = int(input(f'Digite o \033[0:36m{j+1}\033[m ano de nascimento: '))
    ano = date.today().year - ano
    if ano < 21:
        menor += 1
    else:
        maior += 1
print(f'De maior: \033[36m{maior}\033[m\nDe menor: \033[31m{menor}\033[m')

