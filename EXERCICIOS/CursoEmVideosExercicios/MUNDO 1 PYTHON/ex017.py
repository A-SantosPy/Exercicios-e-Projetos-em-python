#cateto e hipotenusa
import math
co = float(input('Coloque o comprimento do cateto oposto: '))
ca = float(input('coloque o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))