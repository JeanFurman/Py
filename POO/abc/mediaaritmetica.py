from media import *


class MediaAritmetica(Media):
    def __init__(self, numeros):
        self.numeros = numeros

    def calcula(self):
        return sum(self.numeros) / len(self.numeros)
