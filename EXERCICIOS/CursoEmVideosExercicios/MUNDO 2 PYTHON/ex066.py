soma = cont = 0
while True:
    num = int(input("DIGITE UM NÚMERO [999 PARA PARAR]: "))
    if num == 999:
        break
    soma += num
    cont += 1
print(f"Você digitou {cont} números e a soma entre eles foi {soma}")