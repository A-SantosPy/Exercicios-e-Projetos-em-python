#seno, cosseno e tangente
from math import cos, sin, tan, radians
a = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print("O ângulo de {} tem o SENO de {:.2f}".format(a,seno))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(a,cosseno))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(a,tangente))


#import math
#a = float(input("coloque um angulo:"))
#seno = math.sin(math.radians(a))
#cosseno = math.cos(math.radians(a))
#tangente = math.tan(math.radians(a))
#print("O ângulo de {} tem o SENO de {:.2f}".format(a,seno))
#print("O ângulo de {} tem o COSSENO de {:.2f}".format(a,cosseno))
#print("O ângulo de {} tem a TANGENTE de {:.2f}".format(a,tangente))