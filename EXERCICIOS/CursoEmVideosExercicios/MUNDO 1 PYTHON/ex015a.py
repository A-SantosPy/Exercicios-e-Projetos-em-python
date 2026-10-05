dias = int(input("quantos dias alugados? "))
km = float(input("quantos kilometros rodados? "))
print("O total a pagar é de R${:.2f}".format(60 * dias + (km * 0.15)))