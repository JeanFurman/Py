def leiaint(n):
    while True:
        try:
            num = int(input(n))
            return num
        except KeyboardInterrupt:
            print(f'\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            num = 0
            return num
        except:
            print(f'\033[31mERRO! Digite um numero inteiro valido!.\033[m')
            continue


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção:\033[m ')
    return opc
