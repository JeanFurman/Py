from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] > 0:
    pessoa['contratacao'] = int(input('Ano de contrataçao: '))
    pessoa['salario'] = float(input('Salario: R$ '))
    pessoa['aposentadoria'] = pessoa['contratacao'] + 35 - nascimento
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')


