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


def leiaFloat(f):
    while True:
        try:
            num = float(input(f))
            return num
        except KeyboardInterrupt:
            print(f'\033[31mUsuario preferiu nao digitar esse numero.\033[m')
            num = 0
            return num
        except:
            print(f'\033[31mERRO! Digite um numero real valido!.\033[m')
            continue


i = leiaint('Digite um numero inteiro: ')
r = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
