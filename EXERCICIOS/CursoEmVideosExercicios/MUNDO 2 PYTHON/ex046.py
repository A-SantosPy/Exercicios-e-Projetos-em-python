#contagem regressiva
from time import sleep
from emoji import emojize

for c in range(10, 0, -1):
    print('Falta {} segundos'.format(c))
    sleep(1)
print(emojize('FOGOS NO CÉU!!!!!!! :sparkle:'))
print('FIM')