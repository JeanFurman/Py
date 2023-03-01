texto = 'Cientista de dados pode ser uma excelente alternativa de carreira.\n'
texto = texto + 'Esse profissionais precisam saber como programar em python.\n'
texto += 'E, claro, devem ser proficientes em Data Science'

import os

arquivo = open(os.path.join('cientista.txt'), 'w')
for palavra in texto.split():
    arquivo.write(palavra + ' ')
arquivo.close()
arquivo = open('cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
# print(conteudo)

######### WITH
with open('cientista.txt', 'r') as arquivo:
    conteudo = arquivo.read()
print(len(conteudo))
print(conteudo)

with open('cientista.txt', 'w') as arquivo:
    arquivo.write(texto[:19])
    arquivo.write('\n')
    arquivo.write(texto[28:66])
arquivo = open('cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)