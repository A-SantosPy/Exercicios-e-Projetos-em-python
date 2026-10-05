#criar um hogo simples de adivinho 

import random
jogador = 0
computador = random.randint(1, 20)

while jogador != computador:
    jogador = int(input('ADVINHE O NUMERO: '))
    print("tente novamente")

print(f'Os numeros jogados foram:\njogador = ({jogador}) x computador = ({computador})')
