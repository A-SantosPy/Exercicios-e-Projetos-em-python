#faça um algoritimo que leia o preço de um produto, e mostre seu novo preço com 5% de desconto
p = float(input('Qual o preço do produto? R$'))
d = p - (p * 5) / 100
print("O produto com 5% de desconto irá ficar R${:.2f}".format(d))