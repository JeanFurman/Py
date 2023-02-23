exp = str(input('Digite a expressao: ')).replace(' ', '')
lista = list()
for f in range(0, len(exp)):
    lista.append(exp[f])
controle = 0
for j in lista:
    if j == '(':
        controle += 1
    if j == ')':
        controle -= 1
    if controle < 0:
        break
if controle == 0:
    print('Essa expressao esta valida!')
else:
    print('Sua expressao esta errada!')

