dias = int(input("quantos dias alugados? "))
km = float(input("quantos kilometros rodados? "))
carro = 60*dias
print("O total a pagar é de R${:.2f}".format(carro + (km * 0.15)))