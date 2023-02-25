jogador = {}
jogadores = []
while True:
    print('-' * 40)
    jogador['nome'] = str(input('Nome do Jogador: '))
    n = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = list()
    soma = 0
    for a in range(0, n):
        jogador['gols'].append(int(input(f'Quantos gols na partida {a}? ')))
        soma += jogador['gols'][a]
    jogador['total'] = soma
    jogadores.append(jogador.copy())
    jogador.clear()
    r = ' '
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
    if r == 'N':
        break
print('-=' * 42)
print('{:<5}{:<15}{:<15}{:<}'.format('cod', 'nome', 'gols', 'total'))
print('-' * 42)
for x in range(0, len(jogadores)):
    print('{:<5}{:<15}{:<15}{:<}'.format(f'{x}', f'{jogadores[x]["nome"]}',
                          f'{jogadores[x]["gols"]}', f'{jogadores[x]["total"]}'))
while True:
    print('-' * 42)
    aux = int(input('Mostrar dados de qual jogador? '))
    if aux == 999:
        break
    if aux > (len(jogadores)-1) or aux < 0:
        print(f'ERRO! Não existe jogador com código {aux}! Tente novamente')
    else:
        print(f'--LEVANTAMENTO DO JOGADOR {jogadores[aux]["nome"]}:')
        for j in range(0, len(jogadores[aux]['gols'])):
            print('{:>5}'.format(f'No jogo {j} fez {jogadores[aux]["gols"][j]} gols.'))
print('<< VOLTE SEMPRE >>')
