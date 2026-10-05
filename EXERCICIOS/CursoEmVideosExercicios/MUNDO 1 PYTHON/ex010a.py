#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#considere: US$1,00 = R$3,27
x = float(input('Quanto reais você tem na carteira? R$'))
y = x/ 4.92
z = x/ 5.33
print('Com essa quantidade de reais da pra comprar: US${:.2f} e €{:.2f}'.format(y, z))
