preco = float(input('Digite o preço: '))
cod = int(input('Digite 1 para cheque/dinheiro à VISTA\nDigite 2 para cartao à VISTA\n''Digite 3 para 2X no '
                'cartao\nDigite 4 para 3X ou mais no cartao: '))
if cod == 4:
    vezes = int(input('Quantas vezes: '))
if cod == 1:
    preco = preco - (preco * 10/100)
    print(f'Voce ira pagar R$ {preco}')
elif cod == 2:
    preco = preco - (preco * 5/100)
    print(f'Voce ira pagar R$ {preco}')
elif cod == 3:
    print(f'Voce ira pagar  2X de R$ {preco/2} no total sendo R$ {preco}')
elif cod == 4:
    preco = preco + (preco * 20 / 100)
    print(f'Voce ira pagar  {vezes}X de R$ {preco/vezes} no total sendo R$ {preco}')
