num = cont = soma = 0
num = int(input("DIGITE UM NÚMERO [999 PARA PARAR]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("DIGITE UM NÚMERO [999 PARA PARAR]: "))
print("Você digitou {} números e a soma entre eles foi {}".format(cont, soma))
