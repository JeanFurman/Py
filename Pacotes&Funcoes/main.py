import numpy

# print(numpy.sqrt(25))
# print(dir(numpy))

import random

print(random.choice(['Abacate', 'Banana', 'Laranja']))
random.sample(range(100), 10)

import statistics

dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(dados))
print(statistics.median(dados))

import os

print(os.getcwd())

import urllib.request

resposta = urllib.request.urlopen('http://python.org')
print(resposta)
html = resposta.read()
print(html)
