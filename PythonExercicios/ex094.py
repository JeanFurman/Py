people = []
person = {}
idade = 0
while True:
    person['nome'] = str(input('Nome: '))
    s = ' '
    while s != 'M' and s != 'F':
        s = str(input('Sexo: [M/F] ')).upper()[0]
        if s not in 'MF':
            print('ERRO! Por Favor, digite apenas M ou F')
    person['sexo'] = s
    person['idade'] = int(input('Idade: '))
    idade += person['idade']
    people.append(person.copy())
    person.clear()
    r = ' '
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar? [S/N] ')).upper()
    if r == 'N':
        break
print('-=' * 30)
print(f'- O grupo tem {len(people)} pessoas.')
media = idade / len(people)
print(f'- A media de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for m in people:
    if m['sexo'] == 'F':
        print(f'{m["nome"]} ', end='')
print('')
print(f'- Lista de pessoas que estao acima da media:')
for m in people:
    if m['idade'] > media:
        for k, j in m.items():
            print(f'{k} = {j}; ', end='')
        print('')
print('<< ENCERRADO >>')


