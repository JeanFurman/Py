pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['media'] = float(input(f'Media de {pessoa["nome"]}: '))
pessoa['situacao'] = 'Reprovado' if pessoa['media'] < 7 else 'Aprovado'
print(f'Nome é igual a {pessoa["nome"]}')
print(f'Media é igual a {pessoa["media"]}')
print(f'Situaçao é igual a {pessoa["situacao"]}')
