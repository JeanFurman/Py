class Cliente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__enderecos = []


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, n):
        self.__nome = n

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, i):
        self.__idade = i

    def insere_endereco(self, c, e):
        self.__enderecos.append(Endereco(c, e))

    def lista_enderecos(self):
        for endereco in self.__enderecos:
            print(endereco.cidade, endereco.estado)
class Endereco:
    def __init__(self, cidade, estado):
        self.__cidade = cidade
        self.__estado = estado

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, e):
        self.__estado = e

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, c):
        self.__cidade = c

