#faça um algoritimo que leia o preço de um produto, e mostre seu novo preço com 5% de desconto
p = float(input("Qual o preço desse produto? R$"))
print("O preço com 5% de desconto vai ficar R${:.2f}".format(p - (p * 5) / 100))