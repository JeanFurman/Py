from time import sleep


def cadastrar():
    try:
        while True:
            nome = str(input('Nome: '))
            if not nome.isnumeric():
                break
        while True:
            idade = str(input('Idade: '))
            if idade.isnumeric():
                break
            print('\033[31mERRO: por favor, digite um numero inteiro válido.\033[m')
        print(f'Novo registro de {nome} adicionado.')
        arq = open('lista_de_cadastros.txt', 'a')
        cadastro = [nome, idade]
        for a in range(0, 2):
            arq.write(cadastro[a])
            arq.write('\n')
    except:
        print('\033[31mERRO! Ocorreu um erro ao cadastrar!\033[m')


def listar():
    arq = open('lista_de_cadastros.txt')
    leitura = arq.readlines()
    aux1 = 0
    aux2 = 1
    for l in range(0, int(len(leitura)/2)):
        print('{:<30}{:<} anos'.format(leitura[aux1].replace('\n', ''), leitura[aux2].replace('\n', '')))
        aux1 += 2
        aux2 += 2
    sleep(2)

