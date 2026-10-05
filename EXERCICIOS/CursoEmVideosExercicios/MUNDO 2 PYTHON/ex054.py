#programa da maior idade
#peça a data de nascimento de 7 pessoas e diga quantas atingiram a maior idade e quantas ainda não atingiram


from datetime import date, datetime

atual = datetime.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input("Em que ano a {}ª pessoa nasceu: ".format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao total tivemos {}ª pessoas maiores de idade e {}ª pessoas menores de idade!'.format(totmaior, totmenor))