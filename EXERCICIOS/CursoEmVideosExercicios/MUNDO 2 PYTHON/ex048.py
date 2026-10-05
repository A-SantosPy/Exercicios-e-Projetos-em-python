#soma de números ímpares que são múltiplos de 3
# e que se encontram em um intervalo de 1 ate 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos {} os valores solicitados é {}'.format(cont ,soma))
