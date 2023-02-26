def leiaint(n):
    while True:
        num = input(n)
        if num.isdigit():
            return num
        else:
            print(f'\033[31mERRO! Digite um numero inteiro valido!.\033[m')


n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
