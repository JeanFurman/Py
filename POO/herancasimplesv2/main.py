from automovel import *
from moto import *

carro = Automovel(17, 'Hyundai', 500)
carro.ligar_luz_teto()
carro.acelerar()
carro.frear()

moto = Moto(14, 'Honda', 50)
moto.acelerar()
moto.frear()
