from mediaaritmetica import *
from mediageometrica import *

l = [5, 5, 5]
ma = MediaAritmetica(l)
mg = MediaGeometrica(l)

print(f'Media aritmetrica de {l} é {ma.calcula()}')
print(f'Media geometrica de {l} é {mg.calcula()}')
