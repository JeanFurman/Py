from media import *


class MediaGeometrica(Media):
    def __init__(self, numeros):
        self.numeros = numeros

    def calcula(self):
        from math import prod
        return prod(self.numeros) ** (1/len(self.numeros))
