num = int(input('Digite um numero: '))
print('''Escolha uma opçao:
[1] converter para Binario
[2] converter para Octal
[3] converter para Hexadecimal''')
opcao = int(input('Sua opçao: '))
if opcao == 1:
    print(f'Binario: {bin(num)[2:]}')
elif opcao == 2:
    print(f'Octal: {oct(num)[2:]}')
elif opcao == 3:
    print(f'Hexadecimal: {hex(num)[2:]}')
else:
    print('Opcao invalida!')