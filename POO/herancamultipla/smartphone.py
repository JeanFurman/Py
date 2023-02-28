from celular import *
from camera import *
from tablet import *


class Smartphone(Celular, Camera, Tablet):
    def __init__(self, armazenamento, ram, qtde_nucleos):
        Celular.__init__(self)
        Camera.__init__(self)
        Tablet.__init__(self, armazenamento, ram, qtde_nucleos)
