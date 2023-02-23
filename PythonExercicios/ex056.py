media = 0
mulheres = 0
velho = 0
nomev = ''
for j in range(0, 4):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))
    media += idade
    if sexo == 'F':
        if idade < 20:
            mulheres += 1
    else:
        if j == 0:
            velho = idade
            nomev = nome
        else:
            if idade > velho:
                velho = idade
                nomev = nome
print(f'''A media de idade do grupo é {media/4}
O homem mais velho tem {velho} anos e seu nome é {nomev}
Tem {mulheres} mulher(es) com menos de 20 anos''')