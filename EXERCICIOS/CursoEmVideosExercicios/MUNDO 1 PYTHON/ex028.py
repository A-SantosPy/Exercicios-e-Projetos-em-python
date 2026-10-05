import random

print('Jogo da adivinhação :)')

num = random.randint(0, 5) #aqui ele vai randomizar um numero inteiro de 0 a 5
print('Vou pensar em um número de 0 a 5. Chuta qual é') #aqui ele deciciu qual número é ("pensou")
le = int(input('Qual sua resposta? ')) #aqui você responde
if num == le:
    print('Congratulations você acertou skdalk') #se sua resposta estiver certa ele mostra essa mensagem
else:
    print('não foi dessa vez, tente novamente :)') #se estiver errada ele mostra essa mensagem
    print('{}'.format(num)) #aqui era so pra ter certeza que tava funcionando
 