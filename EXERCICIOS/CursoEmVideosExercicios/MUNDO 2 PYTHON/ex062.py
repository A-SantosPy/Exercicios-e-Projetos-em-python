print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input("DIGITE O PRIMEIRO TERMO: "))
razao = int(input("DIGITE A RAZÃO: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print("{} → ".format(termo), end="")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("QUANTOS TERMOS VOCÊ QUER MOSTRAR A MAIS? "))
print("finalizando...")