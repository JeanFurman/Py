from agregacao.compra import CarrinhoDeCompras, Produto2

carrinho = CarrinhoDeCompras()
p1 = Produto2('Camiseta', 50)
p2 = Produto2('iPhone', 10000)
p3 = Produto2('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.lista_produto()
print(carrinho.soma_total())