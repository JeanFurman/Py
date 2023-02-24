from time import sleep
boletim = []
aluno = []
notas = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    notas.append(nota1)
    notas.append(nota2)
    notas.append((nota1 + nota2)/2)
    aluno.append(nome)
    aluno.append(notas[:])
    boletim.append(aluno[:])
    aluno.clear()
    notas.clear()
    r = ''
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar? [S/N] ')).upper()
    if r == 'N':
        break
print('-=' * 40)
print('{:<}{:^10}{: >18}'.format('No.', 'NOME', 'MÉDIA'))
print('-' * 30)
for j in range(0, len(boletim)):
    print('{:<6}{:<20}{:<}'.format(j, boletim[j][0], boletim[j][1][2]))
print('-' * 40)
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if n == 999:
        break
    print(f'Notas de {boletim[n][0]} são [{boletim[n][1][0]}, {boletim[n][1][1]}]')
    print('-' * 40)
print('FINALIZANDO...')
sleep(2)
print('<<< VOLTE SEMPRE >>>')
