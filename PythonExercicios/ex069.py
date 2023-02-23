contIdade = contHomens = contMulheres = idade = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ''
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        contIdade += 1
    if sexo == 'M':
        contHomens += 1
    elif idade < 20:
        contMulheres += 1
    print('-' * 30)
    r = ''
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('===== FIM DO PROGRAMA =======')
print(f'Total de pessoas com mais de 18 anos: {contIdade}')
print(f'Ao todo temos {contHomens} homens cadastrados')
print(f'E temos {contMulheres} mulheres com menos de 20 anos')

