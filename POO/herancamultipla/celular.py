from telefone import *


class Celular(Telefone):
    def __init__(self):
        Telefone.__init__(self)

    def enviar_sms(self):
        print('Ola, tudo bem?')
