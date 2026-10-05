"extraindo dados com pytohn"

lista = []
while True:
    lista.append(int(input("DIGITE UM VALOR: ")))
    resp = str(input("VOCÊ QUER CONTINUAR [S/N]: ")).strip()
    if resp in 'nN':
        break
print(f"Os valores digitados foram {lista}")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são {lista}")
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não foi encontrado na lista')