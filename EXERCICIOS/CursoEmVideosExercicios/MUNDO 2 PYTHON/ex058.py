#jogo da adivinhação 2.0
from random import randint
from time import sleep
computador = randint(0, 10)
tentativa = 0
print('Vamos jogar um jogo? pensei em um número que vai de 0 a 10, consegue adivinhar qual é?')
sleep(2)
acertou = False
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    tentativa += 1
    if jogador == computador:
        acertou = True
        print('Você acertou!')
    elif jogador >= computador:
            print('Um pouco menos')
    elif jogador <= computador:
                print('Um pouco mais')
print('Fim, você tentou {} vezes'.format(tentativa))