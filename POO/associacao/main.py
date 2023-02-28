from associacao.classes import *

escritor = Escritor('Joaozinho')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever()
print(caneta.marca)
escritor.ferramenta = caneta
escritor.ferramenta.escrever()