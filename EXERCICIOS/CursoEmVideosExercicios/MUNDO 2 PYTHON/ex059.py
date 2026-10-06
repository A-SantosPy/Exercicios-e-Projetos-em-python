valor1 = int(input("DIGITE UM VALOR: "))
valor2 = int(input("DIGITE OUTRO VALOR: "))
print("ESCOLHA UMA OPÇÃO: ")
print("[1] SOMAR")
print("[2] MULTIPLICAR")
print("[3] MAIOR")
print("[4] NOVOS NÚMEROS")
print("[5] SAIR DO PROGRAMA")

opcao = 0
while opcao != 5:
    opcao = int(input("DIGITE SUA OPÇÃO: "))
    if opcao == 1:
        soma = valor1 + valor2
        print("A SOMA ENTRE {} + {} É {}".format(valor1, valor2, soma))
    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print("A MULTIPLICAÇÃO ENTRE {} * {} É {}".format(valor1, valor2, multiplicacao))
    elif opcao == 3:
        if valor1 > valor2:
            print("O MAIOR VALOR ENTRE {} E {} É {}".format(valor1, valor2, valor1))
        else:
            print("O MAIOR VALOR ENTRE {} E {} É {}".format(valor1, valor2, valor2))
    elif opcao == 4:
        print("DIGITE NOVOS NÚMEROS")
        valor1 = int(input("DIGITE UM VALOR: "))
        valor2 = int(input("DIGITE OUTRO VALOR: "))
    elif opcao == 5:
        print("FINALIZANDO...")
    else:
        print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE")
    print("-=" * 10)