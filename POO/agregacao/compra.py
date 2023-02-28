class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, p):
        self.produtos.append(p)

    def lista_produto(self):
        for p in self.produtos:
            print(p.nome, p.valor)

    def soma_total(self):
        total = 0
        for p in self.produtos:
            total += p.valor
        return total
class Produto2:
    def __init__(self, nome, val):
        self.nome = nome
        self.valor = val