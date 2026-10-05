p = float(input("qual o preço do produto: R$"))
d = int(input("qual o desconto: %"))
a = p - (p * d / 100)
print("O produto de R${} com {}% de desconto vai ficar: R${}".format(p, d, a))