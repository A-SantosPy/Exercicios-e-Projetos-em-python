#faça um programa que leia uma frase pelo teclado e mostre
#quantas vezes aparece a letra "A"
#em que posição aparece a primeira vez
#em que posição aparece a última vez
frase = str(input("Digite uma frase: ")).upper().strip()
print('a letra A aparece {} vezes na frase'.format(frase.count("A")))
print('a primeira posição que aparece é {}'.format(frase.find("A")+1))
print('a ultima posição que aparece é {}'.format(frase.rfind("A")+1))