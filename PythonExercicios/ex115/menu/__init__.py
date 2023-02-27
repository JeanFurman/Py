from ex115 import processos
from time import sleep
cor = ('\033[m',    # 0 - sem cor / fechamento
       '\033[33m',  # 1 - amarelo
       '\033[34m',  # 2 - azul
       '\033[32m',   # 3 - verde
       '\033[31m'   # 4 - vermelho
       )


def exibir(msg):
    try:
        linhas('MENU PRINCIPAL')
        print(f'''{cor[1]}1{cor[0]} - {cor[2]}Ver pessoas cadastradas{cor[0]}
{cor[1]}2{cor[0]} - {cor[2]}Cadastras nova Pessoa{cor[0]}
{cor[1]}3{cor[0]} - {cor[2]}Sair do Sistema{cor[0]}
    ''')
        print('-' * 40)
        opcao = int(input(f'{cor[3]}Sua opção: {cor[0]}'))
        if opcao == 1:
            linhas('PESSOAS CADASTRADAS')
            processos.listar()
        elif opcao == 2:
            linhas('NOVO CADASTRO')
            processos.cadastrar()
        elif opcao == 3:
            linhas('Saindo do sistema... Até logo!')
            sleep(1)
            return True
        else:
            raise
    except:
        print(f'{cor[4]}ERRO! Digite uma opção válida!{cor[0]}')
        return False


def linhas(msg):
    print('-' * 40)
    print('{:^40}'.format(msg))
    print('-' * 40)
