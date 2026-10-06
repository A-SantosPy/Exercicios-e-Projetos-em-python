n = int(input("DIGITE UM NÚMERO PARA CALCULAR O FATORIAL: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print("O FATORIAL DE {} É {}".format(n, fatorial))
